"""
Backend parse data from client, save data

"""

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

DESCRIPTION = __doc__ or ""
tags_metadata = [
	{
		"name": "Home"
	}
]

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

@app.post("/")
async def parse(item: Item):
	"""
	Parse api
	"""

	# TODO: parse html
	with open('test.html', 'w') as f:
		f.write(item.data)
	return {
		"data": item
	}