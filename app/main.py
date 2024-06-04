#import psycopg2
#from psycopg2.extras import RealDictCursor
from fastapi import FastAPI
#Response, status, HTTPException, Depends
#from fastapi.params import Body 
#from pydantic import BaseModel
#from typing import Optional, List
#from random import randrange
from . import models
#, schemas, utils 
from .database import  engine
#, get_db
#from sqlalchemy.orm import Session
# from sqlalchemy.sql.functions import mode
from .routers import post, user, auth, vote
#from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#pydanctic: to make schema - basically restrict form of data to POST method
#, cursor_factory=RealDictCursor

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

''' 
while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', 
                               user='postgres', password='Solarwaterboat', cursor_factory=RealDictCursor)
        #conn =  psycopg.connect("postgresql://postgres:Solarwaterboat@localhost:5432")

        cursor = conn.cursor()
        print("Database connection was succesful")
        break
    except Exception as error:
        print("Connection failed")
        print("Error: ", error)
''' 

#CORS

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World "}







