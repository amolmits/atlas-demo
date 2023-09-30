import pymongo
import sys

# Replace the placeholder data with your Atlas connection string. Be sure it includes
# a valid username and password! Note that in a production environment,
# you should not store your password in plain-text here.

try:
  client = pymongo.MongoClient("mongodb+srv://dtgcpsyd:GrantAmol@cluster0.ruaemqr.mongodb.net/?retryWrites=true&w=majority")
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use a database named "myDatabase"
db = client.myDatabase

# use a collection named "recipes"
my_collection = db["Interviews"]

name_c1 = input("Candidate Name!\n")
name_p1 = input("Enter Interviewer 1 Name!\n")
name_p2 = input("Enter Interviewer 2 Name!\n")
name_p3 = input("Enter Interviewer 3 Name!\n")
date = input("Enter Interview Date!\n")
feed = input("Enter Feedback!\n")

interview_document = [{"candidate_name":name_c1, "interviewers":[name_p1, name_p2,name_p3], "interview_date":date, "interview_feedback":feed}]

# drop the collection in case it already exists
#try:
#  my_collection.drop()  

# return a friendly error if an authentication error is thrown
#except pymongo.errors.OperationFailure:
#  print("An authentication error was received. Are your username and password correct in your connection string?")
#  sys.exit(1)

# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

try: 
 result = my_collection.insert_many(interview_document)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)
  print("Thank you. Feedback for {} has been recorded.".format(name_c1))
  print("\n")
