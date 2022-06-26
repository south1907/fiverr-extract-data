"""
Backend parse data from client, save data

"""

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup
import json
import os
import pymongo

with open('config.json', 'r') as f:
	config = json.loads(f.read())

MONGO_URI = config['mongo_uri']
MONGO_DATABASE = config['mongo_database']
MONGO_COLLECTION_ITEM = config['mongo_collection']
MONGO_COLLECTION_DETAIL = config['mongo_collection_detail']

myclient = pymongo.MongoClient(MONGO_URI)
mydb = myclient[MONGO_DATABASE]
mycol_item = mydb[MONGO_COLLECTION_ITEM]
mycol_detail = mydb[MONGO_COLLECTION_DETAIL]

DESCRIPTION = __doc__ or ""
tags_metadata = [
	{
		"name": "Home"
	}
]

root_domain = 'https://www.fiverr.com'

app = FastAPI(
	title="Backend parse data",
	description=DESCRIPTION,
	version="1.0",
	openapi_tags=tags_metadata
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["GET", "POST"],
	allow_headers=["*"],
)
class Item(BaseModel):
	data: str
	category: str
	page: int

class ItemUpdate(BaseModel):
	id: int
	data: str
	

@app.get("/", tags=["Home"])
async def index():
	"""
	Home Path for API
	"""
	return {
		"For docs": "Visit /docs"
	}

@app.post("/")
async def parse(item: Item):
	"""
	Parse api
	"""
	text_html = item.data
	soup = BeautifulSoup(text_html, "lxml")
	find = soup.find('script', {'id': 'perseus-initial-props'})
	data = json.loads(find.string)

	gigs = data['listings'][0]['gigs']

	# check
	is_exist = os.path.exists(item.category)

	if not is_exist:
		os.makedirs('data/' + item.category)
		print("create new folder: " + item.category)

	with open('data/' + item.category + "/" + str(item.page) + ".json", "w") as f:
		json.dump(gigs, f, indent=4)

	return {
		"status": True
	}

@app.get("/detail")
async def get_detail():
	"""
	Get 1 url to update detail
	"""
	query = {
		'is_get_detail': {
			'$exists': False
		}
	}
	item = mycol_item.find_one(query)

	if item:
		return {
			"id": item['gigId'],
			"url": root_domain + item['gig_url']
		}

	return {
		"id": None,
		"url": None
	}

@app.post("/update-detail")
async def update_detail(item: ItemUpdate):
	"""
	Parse and update Detail
	"""
	text_html = item.data
	soup = BeautifulSoup(text_html, "lxml")
	find = soup.find('script', {'id': 'perseus-initial-props'})
	data = json.loads(find.string)

	if data:
		mycol_detail.insert_one(data)

		# update done
		myquery = { "gigId": item.id }
		print('update done: ' + str(item.id))
		newvalues = { "$set": { "is_get_detail": 1 } }
		mycol_item.update_many(myquery, newvalues)
		return {
			"status": True,
			"id": item.id
		}

	return {
		"status": False,
		"id": item.id
	}
