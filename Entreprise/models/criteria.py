class Criteria:
    def __init__(self, limit=None, page=None, secteur_activite=None, nom=None, email=None):
        self.limit = limit
        self.page = page
        self.nom = nom
        self.email = email
        self.secteur_activite = secteur_activite
