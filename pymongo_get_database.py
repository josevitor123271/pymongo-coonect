from pymongo import MongoClient

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017/"

    #Create a Client object
    client = MongoClient(CONNECTION_STRING)

    return client['clinica']

if __name__ == "__main__":
    
    # Get the database
    dbname = get_database()
    print(dbname)