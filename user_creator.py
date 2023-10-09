# import packages
from database import engine,User
from sqlalchemy.orm import sessionmaker
import bcrypt

# some nesseccery configs
Session = sessionmaker(bind=engine)
session = Session()

# function to add users
def add_user(email,password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    data=User(email=email,password=hashed_password)
    session.add(data)
    session.commit()


add_user("sin.majidi@gmail.com","123456")