# Team Danger Noodles | Minnehack 2020 
![scratching post logo](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/logo1.png)

## Purpose
**Prompt:**  *develop a solution for local communities to help them foster social good*

There are many local animal adoption shelters in Minneapolis and other cities.  Shown below are a small selection (image from [Google Maps](https://www.google.com/permissions/geoguidelines/))

![map of local shelters](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/map.png)

- These places provide **social good** by taking care of animals and providing a companion to people who adopt these pets.  Pets can provide [health benefits](https://www.cdc.gov/healthypets/health-benefits/index.html).

- The local **communities of volunteers** often create social media posts to advertise pets avaliable for adoption.

- By helping automate content creation, posting can be done more frequently, which means that volunteers will have more time to spend taking care of animals, and more animals will be seen and have a chance at finding a new home.  This helps **foster social good and foster animals**.

## How it Works
Transforms images into posts, with [automatic Tweeting](https://twitter.com/AnimalExample), tagging, and captioning
![infographic](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/infographic1.png)
Data is stored online using mongoDB, so trends can be seen
![catdogpiechart](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/pie.png)
![posts](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/posts.png)

## Technologies Used

 - Google Cloud Vision API label detection: to determine if a photo contains a dog or cat, get relevant hashtags
- [Oxford-IIIT pet dataset](https://www.tensorflow.org/datasets/catalog/oxford_iiit_pet):  for testing
- UiPath Data Scraping: to gather cat and dog puns from these websites:
	- https://www.rover.com/blog/cat-puns/
	- https://www.mydogsname.com/dog-puns/
- mongoDB to store tweet data, and supply data shown using Plotly
- Python Libraries/APIs
	- PyGame
	- Pymongo
	- Plotly
	- Twython
	- os, random, csv, datetime
- Icons free from Iconfinder
- Dog icon by [Icons8](https://icons8.com/icons/set/dog)
- Domain.com used to register scratchingpost.tech for future use

## Example Post
![tweet](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/tweet.png)
## Captioned Images
### Cat
![cat_image](https://github.com/MOLLYBAS/Scratching-Post/blob/master/generated/2020-01-25%2023%3A07%3A08.558913.png)
## Doggo
![dog_image](https://github.com/MOLLYBAS/Scratching-Post/blob/master/generated/2020-01-26%2000:10:27.830547.png)
