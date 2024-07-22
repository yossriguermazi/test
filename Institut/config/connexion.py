import os
from pymongo import MongoClient
from dotenv import load_dotenv

class MongoConnect:
    def __init__(self) -> None:
        load_dotenv()
        self.uri = os.getenv("MONGO_URI")
        self.database_name = os.getenv("DATABASE_NAME")

        if not self.uri or not self.database_name:
            raise ValueError("MONGO_URI and DATABASE_NAME must be set in the environment variables.")

    def init_db(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['Partenaria']
        return client, db
