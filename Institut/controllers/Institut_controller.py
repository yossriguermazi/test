from datetime import datetime
from models.institut_model import InstitutModel
from models.criteria import Criteria


class InstitutController(InstitutModel):
    def __init__(self) -> None:
        super().__init__()

    def findAll(self, criteria: Criteria) -> list:
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
        return InstitutModel.findAll(self, criteria)

    def findOne(self, _id: str):
        return InstitutModel.findOne(self, _id)

    def insert(self, body):
        body["createdAt"], body["updatedAt"] = str(datetime.now()), str(datetime.now())

        result = InstitutModel.insert(self, body)
        return self.findOne(result.inserted_id)

    def update(self, _id: str, body: dict):
        try:
            return InstitutModel.update(self, _id, body)
        except Exception as e:
            raise Exception(f"Document update error: {e}")

    def remove(self, _id: str):
        return InstitutModel.remove(self, _id)


