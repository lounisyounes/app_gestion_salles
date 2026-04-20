from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

#  connexion
conn = dao.get_connection()
if conn.is_connected():
    print("Connexion reussie")
conn.close()

#  ajout
s1 = Salle("S100", "Salle test", "Classe", 20)
dao.insert_salle(s1)
print("Salle ajoutee")

#  modification
s1.libelle = "Salle modifiee"
s1.type = "Laboratoire"
s1.capacite = 25
dao.update_salle(s1)
print("Salle modifiee")

#  recherche
salle = dao.get_salle("S100")
if salle:
    salle.afficher_infos()

#  affichage total
liste = dao.get_salles()
for s in liste:
    s.afficher_infos()

#  suppression
dao.delete_salle("S100")
print("Salle supprimee")