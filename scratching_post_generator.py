import os, random, csv, random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
from datetime import datetime
from twython import Twython
import pymongo

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    dbpw
)

def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels

def is_dog(labels):
    for label in labels:
        if label.description == "Dog":
            return True
    return False

def is_cat(labels):
    for label in labels:
        if label.description == "Cat":
            return True
    return False

def get_dog_pun(data):
    num_dog_puns = 108
    num = random.randint(0,num_dog_puns-1)
    pun = data[num][0]
    nc = 0
    for char in pun:
        if char == ".":
            break
        nc+=1
    pun = pun[nc+2:]
    return pun

def get_cat_pun(data):
    num_cat_puns = 66 # q odd a even up to 65,66
    num = random.randint(0,num_cat_puns-1)
    if num%2 != 0:
        num -= 1
        if num < 0:
            num = 0
    pun = data[num][1]
    nc = 0
    for char in pun:
        if char == ".":
            break
        nc+=1
    pun = pun[nc+2:]
    return [pun, data[num+1][1]]

def display_image(img_path, text):
    font_path = "./fonts/Pacifico.ttf"
    font_size = 20
    # font_path = None
    pygame.init()
    image = pygame.image.load(img_path)
    screen = pygame.display.set_mode(image.get_rect().size, 0, 32)
    image = image.convert()
    screen.blit(image, (0,0))

    pygame.display.set_caption('Scratching Post')
    ofs = 1
 
    if len(text) != 2:
        font = pygame.font.Font(font_path, font_size + 10)
        text1 = font.render(text, 1, (10, 10, 10))
        textw = font.render(text, 1, (250, 250, 250))
        textpos = text1.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textposw = (textpos[0]+ofs, textpos[1]+ofs)
        screen.blit(textw, textposw)
        screen.blit(text1, textpos)
    else:
        font = pygame.font.Font(font_path, font_size)
        text1 = font.render(text[0], 1, (10, 10, 10))
        text2 = font.render(text[1], 1, (10, 10, 10))

        text1w = font.render(text[0], 1, (250, 250, 250))
        text2w = font.render(text[1], 1, (250, 250, 250))


        textpos1 = text1.get_rect()
        textpos2 = text2.get_rect()

        textpos1.centerx = screen.get_rect().centerx
        textpos2.midbottom = screen.get_rect().midbottom

        screen.blit(text1, textpos1)
        screen.blit(text2, textpos2)

        textposw1 = (textpos1[0]+ofs, textpos1[1]+ofs)
        textposw2 = (textpos2[0]+ofs, textpos2[1]+ofs)

        screen.blit(text1w, textposw1)
        screen.blit(text2w, textposw2)

    pygame.display.flip()
    # pygame.image.save(window,"screenshot.png")
    filename = (str(datetime.now())+".png")
    pygame.image.save(screen, (filename))
    pth = "generated/" + filename
    os.rename(filename, pth)
    # print(pth)
    # print("TEST")
    return pth

    # Event loop
    # while 1:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             return

def generate():
    path = random.choice(os.listdir("./images/images"))
    img_path = "./images/images/" + path
    labels = detect_labels(img_path)
    # labels = detect_labels("cat.jpg") # COMMENT TO FIX RAND
    # for label in labels:
    #     print(label.description)

    pun_path = "minnehack_scraped_data.csv"
    csvDataFile = open(pun_path)
    data=list(csv.reader(csvDataFile))

    if is_cat(labels):
        # return # REMOVE TO INCLUDE CATS
        pun = get_cat_pun(data)
    else:
        pun = get_dog_pun(data)
        # return # remove to include dogs
    img_path = display_image(img_path, pun)
    return [img_path, labels]

def tweet(message, img_path):
    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

    image = open(img_path, 'rb')
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]  

    twitter.update_status(status=message, media_ids=media_id)
    print("Tweeted: %s" % message)

def main():
    # for i in range(0,10):
    [img_path, labels] = generate()
    messages = ["Adopt a new friend today!","Come visit me at the shelter!","Hello human!","Avaliable for adoption:","Awe, so cute!"]
    message = random.choice(messages)
    message2 = message
    for u in labels:
        message2 += " #" + str(u.description.split()[0])


    tweet(message2, img_path)
    # print(message2)

    # save to db
    client = pymongo.MongoClient("mongodb+srv://dbUser:" + dbpw + "@cluster0-xap7m.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test

    collection = db['PetDataCollection']
    # sample data
    if is_dog(labels):
        document = {"Family":"Dog","Message":message2,"Path":img_path}
        # insert document into collection
        id = collection.insert_one(document).inserted_id
    if is_cat(labels):
        document = {"Family":"Cat","Message":message2,"Path":img_path}
        # insert document into collection
        id = collection.insert_one(document).inserted_id

if __name__ == '__main__': main()


