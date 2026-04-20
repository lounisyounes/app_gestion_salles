from models.salle import Salle
from services.services_salle import ServiceSalle

service = ServiceSalle()

print("Liste des salles :")
for salle in service.recuperer_salles():
    salle.afficher_infos()

print("Ajout d une salle")
s1 = Salle("S200", "Salle Service", "Classe", 30)
print(service.ajouter_salle(s1))

print("Modification d une salle")
s1.libelle = "Salle Service Modifiee"
s1.type = "Bureau"
s1.capacite = 35
print(service.modifier_salle(s1))

print("Recherche d une salle")
salle = service.rechercher_salle("S200")
if salle:
    salle.afficher_infos()

print("Suppression d une salle")
service.supprimer_salle("S200")
print("Suppression terminee")

