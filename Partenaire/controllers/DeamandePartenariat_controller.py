from datetime import datetime
from models.DemandePartenariat_model import DemandePartenariatModel
from models.criteria import Criteria


class DemandePartenariatController(DemandePartenariatModel):
    def __init__(self) -> None:
        super().__init__()

    def findAll(self, criteria: Criteria) -> list:
        limit = criteria.limit or 10
        page = criteria.page or 1
        if limit > 100 or page < 1:
            raise Exception("Limit must be <= 100\nPage must be > 0")
        skip = (page - 1) * limit
        filter = {}
        if criteria.nom_entreprise:
            filter["nom_entreprise"] = criteria.nom_entreprise
        if criteria.type:
            filter["nom_institut"] = criteria.nom_institut
        if criteria.statut_demande:
            filter["statut_demande"] = criteria.statut_demande
        print(filter)
        return DemandePartenariatModel.findAll(self, criteria)

    def findOne(self, _id: str):
        return DemandePartenariatModel.findOne(self, _id)

    def insert(self, body):
        body["createdAt"], body["updatedAt"] = str(datetime.now()), str(datetime.now())

        result = DemandePartenariatModel.insert(self, body)
        return self.findOne(result.inserted_id)

    def update(self, _id: str, body: dict):
        try:
            return DemandePartenariatModel.update(self, _id, body)
        except Exception as e:
            raise Exception(f"Document update error: {e}")

    def remove(self, _id: str):
        return DemandePartenariatModel.remove(self, _id)


