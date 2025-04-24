from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQlite database URL
SQLALCHEMY_DATABASE_URL ='sqlite:///./products.db'

# Create the database engine

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class

Base = declarative_base()

# Dependency to get the database session

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()