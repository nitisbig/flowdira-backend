import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv('HOST')
DB_IP = os.getenv('DB_IP')

DB_URL = f'postgresql://postgres:{password}@{DB_IP}:{DB_HOST}/postgres'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()