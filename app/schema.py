"""
Transaction Data Model

This module defines the `Transaction` model class using the Pydantic library.
"""

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    """
    Transaction Data Model

    This class represents a transaction data record with properties for user_id, amount, description.
    """
    user_id: int = Field(gt=0, description="The user_id must be greater than zero")
    amount: int = Field(gt=0, description="The amount must be greater than zero")
    description: str

    class Config:
        orm_mode = True
