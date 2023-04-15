# Perform CRUD operations
import pymongo as pm # import pymongo library to integrate mongodb and python
client=pm.MongoClient("mongodb://localhost:27017/") # create a collection
mydb=client["telephone_database"] # create a database
my_col=mydb["CRUP_operations"]# create a collection in that database
# 1)create
# insert some documents in the collection.
data=[{"Name":"Omkar","Phone_No":7400364638,"Place":"Mumbai"},
     {"Name":"Vignesh","Phone_No":9892627278,"Place":"Bangalore"},
     {"Name":"Sejal","Phone_No":8272719187,"Place":"Mumbai"},
     {"Name":"Vidhi","Phone_No":8162581990,"Place":"Bangalore"}]
my_col.insert_many(data) # insert documents into the collection 
for i in my_col.find():
    print(i)

# 2) Retrieve
# if you want to dispaly a specific document.
query={"Name":"Omkar"}
for i in my_col.find(query):
    print(i)

# 3) update
# if you want to update any document.
my_col.update_one({"Name":"Sejal"},{"$set":{"Place":"Noida"}})
for i in my_col.find({"Name":"Sejal"}):
    print(i)
    
# 4)delete
# if you delete any document (delete)
query={"Name":"Vignesh"}
my_col.delete_one(query)
for i in my_col.find():
    print(i)