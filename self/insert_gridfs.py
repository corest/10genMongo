import pymongo
import sys
import gridfs

connection = pymongo.Connection("mongodb://10.180.30.45", safe=True)

db = connection.test
videos_meta = db.videos_meta

def main():
	
	grid = gridfs.GridFS(db, "pdf")
	fin = open("asd.pdf", "r")

	_id = grid.put(fin)
	fin.close()

	print ("id of file is ", _id)

	videos_meta.insert({'grid_id' : _id, "filename" : "asd.pdf"})

main()