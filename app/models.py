from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Product(SQLModel, table=True):
    __table_args__ = {"schema": "SalesLT"}

    ProductID: Optional[int] = Field(default=None, primary_key=True)
    Name: str = Field()
    ProductNumber: str = Field()
    Color: Optional[str] = Field(default=None)
    StandardCost: Optional[float] = Field(default=None)
    ListPrice: Optional[float] = Field(default=None)
    Size: Optional[str] = Field(default=None)
    Weight: Optional[float] = Field(default=None)
    ProductCategoryID: Optional[int] = Field(default=None)
    ProductModelID: Optional[int] = Field(default=None)
    SellStartDate: datetime = Field()
    SellEndDate: Optional[datetime] = Field(default=None)
    DiscontinuedDate: Optional[datetime] = Field(default=None)
    ThumbnailPhotoFileName: Optional[str] = Field(default=None)
    rowguid: str = Field()
    ModifiedDate: datetime = Field()

    # Exclure ThumbNailPhoto car elle contient des données binaires problématiques
