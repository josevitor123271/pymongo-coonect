from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

url = "mongodb+srv://caang2024119tads0019:B7d1vZRO8D9WHG1J@cluster0.54r2ppg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# username: caang2024119tads0019
# password: B7d1vZRO8D9WHG1J

client = MongoClient(url, server_api=ServerApi('1'))

database = client["sample_mflix"]
collection_films = database["movies"]

# Create query
query = {"title": "The Italian"}

try:
    film = collection_films.find_one(query)
    if film:
        print("Film found: ")
        pprint(film)
    else:
        print("Film not found.")

except Exception as error:
    print("Error found. Verify your connection string: ", error)

finally:
    
    # Close connection
    client.close()
