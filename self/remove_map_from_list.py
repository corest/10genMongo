f = [{'scores': [{'score': 82.11742562118049, 'type': 'exam'}, {'score': 49.61295450928224, 'type': 'quiz'}, {'score': 28.86823689842918, 'type': 'homework'}, {'score': 5.861613903793295, 'type': 'homework'}], '_id': 199, 'name': 'Rae Kohout'},
{'scores': [{'score': 11.9075674046519, 'type': 'exam'}, {'score': 20.51879961777022, 'type': 'quiz'}, {'score': 55.85952928204192, 'type': 'homework'}, {'score': 64.85650354990375, 'type': 'homework'}], '_id': 198, 'name': 'Timothy Harrod'}]

for doc in f:
	temp_scores = doc["scores"][2:]
	if temp_scores[0]["score"] > temp_scores[1]["score"]:
		print("first")
		doc["scores"].remove(temp_scores[1])
	else:
		print("second")
		doc["scores"].remove(temp_scores[0])
	print("\n")
	#print(doc)
	
print (f)