from fastapi import FastAPI
from app.routers import products
from app.auth import router as auth_router

app = FastAPI(
    title="Mon API AdventureWorks",
    description="API pour gérer les produits et commandes d'AdventureWorks",
    version="1.0.0",
    docs_url="/docs",  # URL pour Swagger
    redoc_url="/redoc",  # URL pour ReDoc
)

# Route par défaut pour la racine
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API AdventureWorks"}

# Enregistrement des routes pour les produits
app.include_router(products.router, prefix="/products", tags=["Products"])

# Inclure le routeur d'authentification
app.include_router(auth_router, prefix="/auth", tags=["auth"])


#uvicorn app.main:app --reload