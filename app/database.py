from sqlmodel import create_engine, Session

# Lecture des variables d'environnement
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
#print(DATABASE_URL)

# Création de l'engine pour SQLModel
engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


# #Test de connexion
# def test_connection():
#     try:
#         # Ouvrir une session
#         with Session(engine) as session:
#             print("Connexion réussie à la base de données.")
            
#             # Exemple de requête pour vérifier les données
#             query = text("""SELECT TABLE_SCHEMA, TABLE_NAME
# FROM INFORMATION_SCHEMA.TABLES;"""
# )
#             results = session.exec(query).all()

#             # Afficher les résultats
#             print("Résultats de la requête :")
#             for row in results:
#                 print(row)
#     except Exception as e:
#         print(f"Erreur lors de la connexion ou de l'exécution : {e}")

# # Appeler la fonction pour tester
# test_connection()
