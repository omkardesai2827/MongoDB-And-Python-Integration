import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client ["mytaskdatabase"] 
mycol = mydb ["Telephone"] 
document = { "Name": "Omkar", "Phone number": "123-456-7890", "Place": "New York" }
x = mycol.insert_one(document)
for x in mycol.find():
    print (x)
query = { "Name": "Omkar" }
result = mycol.find_one(query)
print(result)
update = { "$set": { "Place": "Toronto" } }
result = mycol.update_one(query, update)
print(result.modified_count)





