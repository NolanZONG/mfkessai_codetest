"""
Database Configuration using SQLAlchemy

This module sets up the configuration for connecting to a MySQL database using SQLAlchemy.
It creates a SQLAlchemy engine and session maker for establishing connections and managing sessions.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root@127.0.0.1/codetest"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, pool_size=30, max_overflow=30)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
