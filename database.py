from sqlalchemy import create_engine,Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
# Replace 'database_name.db' with the name you want for your SQLite database
engine = create_engine('sqlite:///database.db')

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
class Ram_data(Base):
    __tablename__ = 'ram_data'
    id = Column(Integer, primary_key=True)
    total = Column(String)
    available = Column(String)
    used=Column(String)
    time=Column(DateTime, default=datetime.datetime.now)

Base.metadata.create_all(engine)