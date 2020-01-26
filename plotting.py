import os, random, csv, random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
from datetime import datetime
from twython import Twython
import pymongo
import plotly.graph_objects as go

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    dbpw
)


client = pymongo.MongoClient("mongodb+srv://dbUser:" + dbpw + "@cluster0-xap7m.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

collection = db['PetDataCollection']

num_cats = 0
num_dogs = 0

# document = {"Family":"Dog","Message":message2,"Path":img_path}
for doc in collection.find({"Family":"Dog"}):
    num_dogs += 1
    print("dog")

for doc in collection.find({"Family":"Cat"}):
    num_cats += 1
    print("cat")





labels = ['Cats','Dogs']
values = [num_cats, num_dogs]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()