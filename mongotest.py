import pymongo
client = pymongo.MongoClient("mongodb+srv://Soumenkhatua:<skhatua2000>@cluster0.6vx9olq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d  = {
    "name" : "soumen" ,
    "email":"soumen@ineuron" ,
    "surname":"khatua"
}

db1 = client['mongoset']
coll = db1['test']
coll.insert_one(d)


