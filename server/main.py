"""
Backend parse data from client, save data

"""

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup
import json

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


@app.get("/", tags=["Home"])
async def index():
	"""
	Home Path for API
	"""
	return {
		"For docs": "Visit /docs"
	}


class Item(BaseModel):
	data: str
	category: str
	page: int

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


	with open('data/' + item.category + "/" + str(item.page) + ".json", "w") as f:
		json.dump(gigs, f, indent=4)

	return {
		"status": True
	}

