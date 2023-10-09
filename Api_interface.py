# import packages
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from database import User,engine,Ram_data
from sqlalchemy.orm import sessionmaker
import bcrypt
import os


# make app
app = FastAPI()
# set a current user for protecting
current_user=None

# some nesseccery config
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
Session = sessionmaker(bind=engine)
security = HTTPBasic()




def get_user_by_email(email: str):
    session = Session()
    user = session.query(User).filter(User.email == email).first()
    session.close()
    return user




# Function to validate basic authentication
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user=get_user_by_email(credentials.username)
    if user and bcrypt.checkpw(credentials.password.encode('utf-8'),
                               user.password.encode('utf-8')):
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed",
            headers={"WWW-Authenticate": "Basic"},
        )

# Route to login
@app.get("/login")
async def login(user: HTTPBasicCredentials = Depends(authenticate_user)):
    global current_user
    current_user=user
    return {"message": "you are logged in"}

# Route to get ram data
@app.get("/get_ram_data/")
async def get_ram_data(limit: int = 5):
    if current_user:
        if limit <= 0:
            raise HTTPException(status_code=400, detail="Limit must be a positive integer")

        session = Session()
        try:
            # Query the last N rows from the ram_data table
            data = session.query(Ram_data).order_by(Ram_data.time.desc()).limit(limit).all()

            # Serialize the data
            final_data = []
            for row in data:
                row_data = {}
                row_data['total'] = row.total
                row_data['used'] = row.used
                row_data['available']=row.available
                final_data.append(row_data)
            return ({'ram_data': final_data})


        finally:
            session.close()
    else:
        return ({"message":"you don't have permission to access api"})