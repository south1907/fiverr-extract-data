import pymongo
import json
import os
import pandas as pd
from datetime import datetime

root_domain = 'https://www.fiverr.com'

with open('config.json', 'r') as f:
	config = json.loads(f.read())

MONGO_URI = config['mongo_uri']
MONGO_DATABASE = config['mongo_database']
MONGO_COLLECTION = config['mongo_collection']
MONGO_COLLECTION_DETAIL = config['mongo_collection_detail']

myclient = pymongo.MongoClient(MONGO_URI)
mydb = myclient[MONGO_DATABASE]
mycol = mydb[MONGO_COLLECTION]
mycol_detail = mydb[MONGO_COLLECTION_DETAIL]

find = mycol_detail.find()

results = []
for i in find:
	if 'general' not in i:
		continue
	general = i['general']
	seller = i['sellerCard']
	username = i['outOfOffice']['username']
	price = i['openGraph']['price']

	member_since = datetime.fromtimestamp(seller['memberSince']).strftime('%d-%m-%y')

	row = [general['gigId'], general['gigTitle'], username, seller['countryCode'], member_since, seller['description'], root_domain + i['portfolio']['slug'], price, i['description']['content']]

	results.append(row)
	# break

df = pd.DataFrame(results, columns=['id', 'title', 'username', 'countryCode', 'member_since', 'memberDescription', 'link', 'price', 'description'])
df.to_excel('data/result.xlsx', engine='xlsxwriter')