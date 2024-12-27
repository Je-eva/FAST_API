from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the SQLite database URL
# SQLite is used as the database engine, and `books.db` is the database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create a SQLAlchemy engine instance
# `connect_args` is required for SQLite to avoid issues with threading
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory bound to the engine
# `autocommit` is set to False to manage transactions manually
# `autoflush` is set to False to avoid premature flushing of changes to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for ORM models
# This is the foundation for defining database models using SQLAlchemy
Base = declarative_base()
