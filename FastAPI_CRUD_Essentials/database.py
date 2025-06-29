#This is from step 6===================================================================================================
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

INIT_ENGINE = create_engine("mysql+pymysql://root:YOUR_PASSWORD@localhost", isolation_level="AUTOCOMMIT")

with INIT_ENGINE.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS UsersDemo"))

#DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/mydatabase"
DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost/UsersDemo"


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
