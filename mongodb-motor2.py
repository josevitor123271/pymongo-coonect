import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from pprint import pprint

url = "mongodb+srv://caang2024119tads0019:n04k7hGgZ9NLbozk@zeneto.0rjs15h.mongodb.net/sample_mflix?retryWrites=true&w=majority&appName=ZeNeto"

async def busque_filmes():
    client = AsyncIOMotorClient(url, server_api=ServerApi('1'))
    
    try:
        database = client['sample_mflix']
        collection_movies = database['movies']
        
        query = {"title": "A Corner in Wheat"}

        film = await collection_movies.find_one(query)
        if film:
            print(film)
        else:
            pprint("No film found!")
            
    except Exception as error:
        print(error)
    finally:
        client.close()

asyncio.run(busque_filmes())