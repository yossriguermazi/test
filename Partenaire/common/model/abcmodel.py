from abc import ABC, abstractmethod

class ABCDemandePartenariat(ABC):
    nom_entreprise: str
    nom_institut: str
    date_demande: str
    objet: str
    description_partenariat: str
    avantages_institut: str
    avantages_entreprise: int
    duree_partenariat: int
    representant_entreprise: dict
    statut_demande: dict
    commentaires: dict

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
