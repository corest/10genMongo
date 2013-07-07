import pymongo
import sys
import gridfs

connection = pymongo.Connection("mongodb://10.180.30.45", safe=True)


# def getNextSequence(): 

# 	ret = db.counters.find_and_modify(
# 		{
# 			{ "_id" : "name"},
# 			{ "$inc" : { "seq" : 1 }},
# 			 } )
# 	return ret.seq	

def insert( insert_type ):
	db = connection.school
	students = db.students
	# #auto increment
	# counters = db.counters
	# #iinitial insert
	# counters.insert( 
	# 		{ 
	# 			"_id" : "userid",
	# 			"seq" : 0 
	# 		} 
	# 	)

	students = [ { "name" : "Andrew Erlichson", "teachers" : [ 0, 1 ] } ,
			{ "name" : "Richard Kreuter", "teachers" : [ 0, 1, 3] } ,
			{ "name" : "Eliot Horowitz", "teachers" : [ 1, 2, 3 ] } ,
			{ "name" : "MArk Keinrich", "teachers" : [ 0, 3 ] } ]
	
	teachers = [{ "name" : "Mark Horowitz" }, 
				{ "name" : "John Henessy" }, 
				{ "name" : "Bruce Wolley" }, 
				{ "name" : " James Plummer" } ]

	#id
	id_val = 0

	if insert_type == 0:
		work_collection = db.students
		work_list = students
	else:
		work_collection = db.teachers
		work_list = teachers

	for doc in work_list:
		doc["_id"] = id_val
		try:
			work_collection.insert(doc)
		except:
			print ("Error insertion ", sys.exc_info()[0])
		id_val += 1

#insert(0)
#insert(1)
