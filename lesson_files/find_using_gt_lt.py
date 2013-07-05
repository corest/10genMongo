
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://10.180.30.45", safe=True)

# get a handle to the school database
db=connection.school
scores = db.scores


def find():

    print ("find, reporting for duty")

    query = {'type':'exam', 'score':{'$gt':50, '$lt':70}}
    selector = {'_id' : 0}

    try:
        iter = scores.find(query,selector)

    except:
        print ("Unexpected error:", sys.exc_info()[0])

    sanity = 0
    for doc in iter:
        print (doc)
        sanity += 1
        if (sanity > 10):
            break
        

find() 

