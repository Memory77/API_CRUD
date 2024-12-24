from sqlmodel import Session, select
from app.models import Product

def get_all_products(session: Session, limit: int = 100):
    """Récupérer tous les produits avec une limite."""
    return session.exec(select(Product).limit(limit)).all()

def get_product_by_id(session: Session, product_id: int):
    """Récupérer un produit par son ID."""
    product = session.exec(select(Product).where(Product.ProductID == product_id)).first()
    return product

def create_product(session: Session, product_data: Product):
    """Créer un nouveau produit."""
    session.add(product_data)
    session.commit()
    session.refresh(product_data)
    return product_data

def update_product(session: Session, product_id: int, product_data: dict):
    """Mettre à jour un produit existant."""
    product = session.exec(select(Product).where(Product.ProductID == product_id)).first()
    if product:
        for key, value in product_data.items():
            setattr(product, key, value)
        session.commit()
        session.refresh(product)
    return product

def delete_product(session: Session, product_id: int):
    """Supprimer un produit."""
    product = session.exec(select(Product).where(Product.ProductID == product_id)).first()
    if product:
        session.delete(product)
        session.commit()
    return product
