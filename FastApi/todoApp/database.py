# database connection with orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# engine wil be used in either areas of our app
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# instanceof a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# to create each database model in future
Base = declarative_base()
