import pymongo
import json
import os

with open('config.json', 'r') as f:
	config = json.loads(f.read())

MONGO_URI = config['mongo_uri']
MONGO_DATABASE = config['mongo_database']
MONGO_COLLECTION = config['mongo_collection']

myclient = pymongo.MongoClient(MONGO_URI)
mydb = myclient[MONGO_DATABASE]
mycol = mydb[MONGO_COLLECTION]

# read folder data
list_item = []

folder_data = config['folder_data']
for file in os.listdir(folder_data):
	if file.endswith(".json"):
		file_path = f"{folder_data}/{file}"
		with open(file_path, 'r') as df:
			data_file = json.loads(df.read())

		list_item.extend(data_file)

mycol.insert_many(list_item)