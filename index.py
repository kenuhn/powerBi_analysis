import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kenuhn:banane@fifadb.oyevc83.mongodb.net/?retryWrites=true&w=majority"
dtype_dict = {'col_108': str}

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

df = pd.read_csv('male_players.csv', index_col="player_id")
documents = df.to_dict('records')
cursor = client['fifa']['malePlayers']
cursor.insert_many(documents)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    cursor = client['fifa']['malePlayers']
    print(cursor)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
