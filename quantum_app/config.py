import pymongo
# Provide the mongodb localhost url to connect python to mongodb.
mongo_client = pymongo.MongoClient("mongodb+srv://prasadilla42:qubit12345@qubitdb.trilvee.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME = "qubitdb"
qubit_db = mongo_client[DATABASE_NAME]


