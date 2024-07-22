from abc import ABC, abstractmethod
from datetime import datetime


class ABCEntreprise(ABC):
    nom: str
    adresse: str
    telephone: str
    email: str
    site_web: str
    date_Fondation: datetime
    secteur_activite: str
    nombre_employees: int
    chiffre_affaires: int
    engagement_entrprise: str


    @abstractmethod
    def findAll(self, **kwargs) -> list[dict] | list: ...

    @abstractmethod
    def findOne(self, _id: str, **kwargs) -> dict: ...

    @abstractmethod
    def insert(self, body: dict, **kwargs) -> dict: ...

    @abstractmethod
    def update(self, body: dict, **kwargs) -> dict: ...

    @abstractmethod
    def remove(self, _id: str, **kwargs) -> dict: ...
