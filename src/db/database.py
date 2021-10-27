from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQL CONNECTION URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test123@localhost/aadhar"

# CREATING ENGINE
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SesssionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engine)

# BASE CREATION
Base  = declarative_base()



# DEPENDENCY INJECTION STEP

def get_db():
    db = SesssionLocal()
    try:
        yield db
    except:
        db.close()