import pymongo
import sys


connection = pymongo.Connection("mongodb://10.180.30.45", safe=True)

def main():
	db = connection.school
	students = db.students

	students_map = students.find()

	try:
		for doc in students_map:
			temp_scores = doc["scores"][2:]
			if temp_scores[0]["score"] > temp_scores[1]["score"]:
				#print("first")
				doc["scores"].remove(temp_scores[1])			
			else:
				#print("second")
				doc["scores"].remove(temp_scores[0])
			students.update({"_id" : doc["_id"]},{ "$set" : { "scores" : doc["scores"] }})
	except:
		print ("Error: ", sys.exc_info()[0])

main()