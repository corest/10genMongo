
import json
from urllib.request import urlopen, ProxyHandler
import pymongo

# connect to mongo
connection = pymongo.Connection("mongodb://10.180.30.45", safe=True)

# get a handle to the reddit database
db=connection.reddit
stories = db.stories

# get the reddit home page
ProxyHandler = {'http': 'http://10.180.30.39:808'}
reddit_page = urlopen("http://www.reddit.com/r/technology/.json")
encoding = reddit_page.headers.get_content_charset()

# parse the json into python objects
parsed = json.loads(reddit_page.read().decode(encoding))


# iterate through every news item on the page
# for item in parsed['data']['children']:
#     # put it in mongo
#     stories.insert(item['data'])


cursor = stories.find()
for doc in cursor:
	print (doc)
