from datetime import datetime
from models.criteria import Criteria
from models.entreprise_model import EntrepriseModel


class EntrepriseController(EntrepriseModel):
    def __init__(self) -> None:
        super().__init__()

    def findAll(self, criteria: Criteria) -> list:
        limit = criteria.limit or 10
        page = criteria.page or 1
        if limit > 100 or page < 1:
            raise Exception("Limit must be <= 100\nPage must be > 0")
        skip = (page - 1) * limit
        filter = {}
        if criteria.nom:
            filter["nom"] = criteria.nom
        if criteria.email:
            filter["email"] = criteria.email
        if criteria.secteur_activite:
            filter["secteur_activite"] = criteria.secteur_activite
        print(filter)
        return EntrepriseModel.findAll(self, criteria)

    def findOne(self, _id: str):
        return EntrepriseModel.findOne(self, _id)

    def insert(self, body):
        body["createdAt"], body["updatedAt"] = str(datetime.now()), str(datetime.now())

        result = EntrepriseModel.insert(self, body)
        return self.findOne(result.inserted_id)

    def update(self, _id: str, body: dict):
        try:
            return EntrepriseModel.update(self, _id, body)
        except Exception as e:
            raise Exception(f"Document update error: {e}")

    def remove(self, _id: str):
        return EntrepriseModel.remove(self, _id)


