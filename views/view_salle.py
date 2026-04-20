import customtkinter as ctk
from services.services_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("600x400")

        self.service_salle = ServiceSalle()