from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DBKEY = os.getenv('DBKEY') 

SQLALCHEMY_DATABASE_URL = rf"postgresql://postgres:{DBKEY}@localhost/ToDoApplicationDB"

engine = create_engine(SQLALCHEMY_DATABASE_URL, client_encoding='utf8')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()