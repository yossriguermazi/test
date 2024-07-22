from config.connexion import MongoConnect
from common.model.abcmodel import ABCDemandePartenariat
from bson import ObjectId
from pymongo import ReturnDocument
from models.criteria import Criteria


class DemandePartenariatModel(ABCDemandePartenariat, MongoConnect):
    def __init__(self) -> None:
        MongoConnect().__init__()
        super().__init__()
        self.client, self.db = self.init_db()
        self.collection_name = "DemandePartenariatModel"

    def findAll(self, criteria: Criteria) -> list[ABCDemandePartenariat]:
        limit = criteria.limit or 10
        page = criteria.page or 1
        if limit > 100 or page < 1:
            raise Exception("Limit must be <= 100\nPage must be > 0")
        skip = (page - 1) * limit
        filter = {}
        if criteria.nom_entreprise:
            filter["nom_entreprise"] = criteria.nom_entreprise
        if criteria.nom_institut:
            filter["nom_institut"] = criteria.nom_institut
        if criteria.statut_demande:
            filter["statut_demande"] = criteria.statut_demande
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

    def update(self, _id: str, body: dict) -> ABCDemandePartenariat:
        _id = body.pop("_id").get("$oid")
        return self.db[self.collection_name].find_one_and_update(
            filter={"_id": ObjectId(_id)},
            update={"$set": body},
            return_document=ReturnDocument.AFTER,
        )

    def remove(self, _id: str) -> ABCDemandePartenariat:
        return self.db[self.collection_name].find_one_and_delete(filter={"_id": ObjectId(_id)})
