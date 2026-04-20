import json
import mysql.connector
from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r") as file:
            config = json.load(file)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        values = (salle.libelle, salle.type, salle.capacite, salle.code)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM salle WHERE code=%s"
        cursor.execute(query, (code,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM salle WHERE code=%s"
        cursor.execute(query, (code,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return Salle(row[0], row[1], row[2], row[3])
        return None