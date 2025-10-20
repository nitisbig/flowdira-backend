from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

passoword = quote_plus('Nitesh!1')

DB_URL = f'postgresql://postgres:{passoword}@34.63.211.31:5432/postgres'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()