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
    
client = pymongo.MongoClient("mongodb+srv://dbUser:" + dbpw + "@cluster0-xap7m.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# define collection
collection = db['SampleCollection']
# sample data
document = {"company":"Capital One","city":"McLean","state":"VA","country":"US"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
print(id)