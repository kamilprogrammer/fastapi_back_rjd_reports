from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = "mysql+pymysql://sql12727459:DTYlnc3Djk@sql12.freemysqlhosting.net:3306/sql12727459"

engine = create_engine(URL_DATABASE)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()














