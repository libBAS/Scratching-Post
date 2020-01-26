import os, random, csv, random

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

path = random.choice(os.listdir("./images/images"))
labels = detect_labels("./images/images/" + path)
# labels = detect_labels("cat.jpg")
for label in labels:
    print(label.description)
print(is_dog(labels))
print(is_cat(labels))
# print("next")
# detect_labels("dog.jpg")

pun_path = "minnehack_scraped_data.csv"
csvDataFile = open(pun_path)
data=list(csv.reader(csvDataFile))


print(data[0])
print(get_dog_pun(data))
print(get_dog_pun(data))
print(get_dog_pun(data))
print(get_dog_pun(data))
print(get_dog_pun(data))

print(get_cat_pun(data))
print(get_cat_pun(data))
print(get_cat_pun(data))
print(get_cat_pun(data))
