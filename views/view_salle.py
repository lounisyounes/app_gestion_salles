import customtkinter as ctk
from services.services_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("600x400")

        self.service_salle = ServiceSalle()

        # Cadre Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadreInfo, text="Code salle").grid(row=0, column=0, padx=10, pady=5)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Libelle").grid(row=1, column=0, padx=10, pady=5)
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Type").grid(row=2, column=0, padx=10, pady=5)
        self.entry_type = ctk.CTkEntry(self.cadreInfo)
        self.entry_type.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Capacite").grid(row=3, column=0, padx=10, pady=5)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)

        # Cadre Actions
        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)