#get_session : Cette fonction (déjà configurée dans database.py) fournit une session à chaque requête.
#select(Product) : Cette requête récupère tous les produits depuis la table SalesLT.Product.
#Depends(get_session) : Cela injecte automatiquement une session SQLAlchemy à chaque requête.
#Retour : produits renvoyés directement au format JSON grâce à la conversion automatique de FastAPI.

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.models import Product
from app.crud.products import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)
from app.auth import get_current_user

router = APIRouter()

@router.get("/", response_model_exclude={"ThumbNailPhoto"})
def read_products(session: Session = Depends(get_session), user: dict = Depends(get_current_user), limit: int = 100):
    products = get_all_products(session, limit)
    return products

@router.get("/{product_id}", response_model_exclude={"ThumbNailPhoto"})
def read_product(product_id: int, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    product = get_product_by_id(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model_exclude={"ThumbNailPhoto"}, status_code=201)
def create_product_endpoint(product: Product, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    created_product = create_product(session, product)
    return created_product

@router.put("/{product_id}", response_model_exclude={"ThumbNailPhoto"}, status_code=200)
def update_product_endpoint(product_id: int, product_data: dict, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    updated_product = update_product(session, product_id, product_data)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=204)
def delete_product_endpoint(product_id: int, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    deleted_product = delete_product(session, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
