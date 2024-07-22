from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime


class ABCInstitut(ABC):
    nom: str
    adresse: str
    telephone: str
    email: str
    site_web: str
    type_institut: str
    nombre_etudiants: int
    nombre_professeurs: int
    country: dict

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
