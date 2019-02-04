import pymongo
def connectDB(collectionName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["demoappdb"]
    mycol = mydb[collectionName]
    return mycol 