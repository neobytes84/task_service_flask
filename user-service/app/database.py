from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQlite database URL
SQLALCHEMY_DATABASE_URL ='sqlite:///database.db'

#Create a SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Create a configured sessionmaker for our database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Create a base class for declarative class definitions
Base = declarative_base()

# Dependency to get the database session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()