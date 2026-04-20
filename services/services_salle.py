from Data.dao_salle import DataSalle
from models.salle import Salle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
            return False, "Tous les champs sont obligatoires"

        if int(salle.capacite) < 1:
            return False, "La capacite doit etre superieure ou egale a 1"

        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutee avec succes"

    def modifier_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
            return False, "Tous les champs sont obligatoires"

        if int(salle.capacite) < 1:
            return False, "La capacite doit etre superieure ou egale a 1"

        self.dao_salle.update_salle(salle)
        return True, "Salle modifiee avec succes"

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)

    def rechercher_salle(self, code):
        return self.dao_salle.get_salle(code)

    def recuperer_salles(self):
        return self.dao_salle.get_salles()