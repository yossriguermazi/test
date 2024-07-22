class Criteria:
    def __init__(self, limit=None, page=None, nom_entreprise=None, nom_institut=None, statut_demande=None):
        self.limit = limit
        self.page = page
        self.nom_entreprise = nom_entreprise
        self.nom_institut = nom_institut
        self.statut_demande = statut_demande
