"""
Data Models

This module defines SQLAlchemy models for fetching/storing transaction data in the MySQL database.
"""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    """
    represents a table named "users"
    """
    __tablename__ = "users"

    id = Column(INTEGER(unsigned=True), primary_key=True, nullable=False, index=True)
    name = Column(String(128), nullable=False)
    api_key = Column(String(256), nullable=False, unique=True)

    transactions = relationship("Transaction", back_populates="owner")


class Transaction(Base):
    """
    represents a table named "transactions"
    """
    __tablename__ = "transactions"

    id = Column(INTEGER(unsigned=True), primary_key=True, nullable=False, index=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey("users.id"), nullable=False)
    amount = Column(INTEGER, nullable=False)
    description = Column(String(256), nullable=False)

    owner = relationship("User", back_populates="transactions")
