from config.connexion import MongoConnect
from common.model.abcmodel import ABCInstitut
from bson import ObjectId
from pymongo import ReturnDocument
from models.criteria import Criteria


class InstitutModel(ABCInstitut, MongoConnect):
    def __init__(self) -> None:
        MongoConnect().__init__()
        super().__init__()
        self.client, self.db = self.init_db()
        self.collection_name = "institutModel"

    def findAll(self, criteria: Criteria) -> list[ABCInstitut]:
        limit = criteria.limit or 10
        page = criteria.page or 1
        if limit > 100 or page < 1:
            raise Exception("Limit must be <= 100\nPage must be > 0")
        skip = (page - 1) * limit
        filter = {}
        if criteria.name:
            filter["name"] = criteria.name
        if criteria.type:
            filter["type"] = criteria.type
        if criteria.countryName:
            filter["country.countryName"] = criteria.countryName
        print(filter)
        return list(
            self.db[self.collection_name]
            .find(filter=filter)
            .skip(skip)
            .limit(limit)
        )

    def findOne(self, _id: str):
        return self.db[self.collection_name].find_one(filter={"_id": ObjectId(_id)})

    def insert(self, body):
        return self.db[self.collection_name].insert_one(body)

    def update(self, _id: str, body: dict) -> ABCInstitut:
        _id = body.pop("_id").get("$oid")
        return self.db[self.collection_name].find_one_and_update(
            filter={"_id": ObjectId(_id)},
            update={"$set": body},
            return_document=ReturnDocument.AFTER,
        )

    def remove(self, _id: str) -> ABCInstitut:
        return self.db[self.collection_name].find_one_and_delete(filter={"_id": ObjectId(_id)})
