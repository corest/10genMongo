import pymongo
import pymysql
import psycopg2
import cql

def main():

    connection = pymongo.MongoClient("mongodb://10.180.30.45")

    db = connection.m101
    people = db.people

    person = {'name':'Barack Obama', 'role':'President',
              'address': {'address1': 'The White House',
                          'street': '1600 Pennsylvania Avenue',
                          'state' : 'DC',
                          'city': 'Washington'},
              'interests':['government', 'basketball', 'the Middle East']}

    people.insert(person)


main()

