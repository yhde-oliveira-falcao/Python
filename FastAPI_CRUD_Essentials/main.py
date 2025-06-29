#Step 1==================================================================================================================
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/hello") #---> got o http://127.0.0.1:8000/hello
def hello_world():
    return("Hello World")

#Step 2==================================================================================================================
@app.get("/hello/{user}") #---> got o http://127.0.0.1:8000/hello/type_your_username
# can also be like: @app.get("/hello/{user}") but the URL request will be like: http://127.0.0.1:8000/hello?=Yuri --> this is the most common for public URL since it keeps the arguments separated from subfolders or levels syntax.
def hello_user(user: str):
    return(f"Bello {user}")

#Step 3==================================================================================================================
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    nationality: str
    income: int

users_db = [] #this will be lost the moment the app is reloaded (any save we do). So next steps will be to create a database

#Step 4==================================================================================================================
@app.post("/user")
async def create_user(user: User):
    #Return the user created only:
    #return {f"User {user} created"}
    users_db.append(user)
    #Return and redirect to the page that displays the User created
    return RedirectResponse(url=f"/hello/{user.name}", status_code=303)


#Step 5==================================================================================================================
@app.get("/users/")
def list_users():
    return users_db


# Step 6==================================================================================================================
    # create a database.py file
    # Create a folder "models" and inside that create a userModels.py
from database import SessionLocal, engine
import models
models.Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#step 7==================================================================================================================
#Add the users to our DB
@app.post("/user_add_db")
def create_user_db(user: User, db: Session = Depends(get_db)):
    #first let's check if the user exists (here we use unique for names)
    existing = db.query(models.User).filter_by(name=user.name).first()
    if existing:
        return {f"User {user.name} already exists in DB"}

    db_user = models.User(name = user.name, age = user.age, nationality = user.nationality, income = user.income)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    #return RedirectResponse(url=f"/hello/{user.name}", status_code=303)
    #return a JSON response
    return {
        "message": f"User {db_user.name} created successfully.",
        "user_id": db_user.id,
    }

#Step 8==================================================================================================================
#GET query all the users
@app.get("/users_db")
def list_users_db(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

#Step 9==================================================================================================================
#Update existing users :)
class UserUpdate(BaseModel):
    age: int
    nationality: str
    income: int

@app.put("/user_update/{name}")
def update_user(name: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    #first we need to find the user in the db
    db_user = db.query(models.User).filter_by(name=name).first()
    if not db_user:
        return {"error": f"User {name} not found"}
    db_user.age = user_update.age
    db_user.nationality = user_update.nationality
    db_user.income = user_update.income

    db.commit()
    db.refresh(db_user)

    return {
        "message": f"User {name} updated",
        "updated_user": {
            "age": db_user.age,
            "nationality": db_user.nationality,
            "income": db_user.income
        }
    }

#Step 10=================================================================================================================
#First step is to define the class (same as previous -> an inputholder class, but in this one all the fields are optional)
from typing import Optional
class UserPatch(BaseModel):
    age: Optional[int] = None
    nationality: Optional[str] = None
    income: Optional[int] = None

@app.patch("/patch_user/{name}")  #copy/paste most of the stuff from previous request/step then change to the "user_patch" class ;) but add conditions for each if not None!
def patch_user(name:str, user_patch: UserPatch, db: Session = Depends(get_db)):
    # first we need to find the user in the db
    db_user = db.query(models.User).filter_by(name=name).first()
    if not db_user:
        return {"error": f"User {name} not found"}
    if user_patch.age is not None:
        db_user.age = user_patch.age
    if user_patch.nationality is not None:
        db_user.nationality = user_patch.nationality
    if user_patch.income is not None:
        db_user.income = user_patch.income

    db.commit()
    db.refresh(db_user)

    return {
        "message": f"User {name} patched nicelly",
        "updated_user": {
            "age": db_user.age,
            "nationality": db_user.nationality,
            "income": db_user.income
        }
    }

#Step 11=================================================================================================================
#Delete an user ;)
@app.delete("/delete/{name}")
def delete_user(name:str, db: Session = Depends(get_db)):
    #first check if user exists (again)
    db_user = db.query(models.User).filter_by(name=name).first()
    if not db_user:
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User '{name}' not found") #THE BEST PRACTICE
        return {"error": f"User {name} not found"}
    db.delete(db_user)
    db.commit()
    return {"message": f"User {name} has been deleted"}
