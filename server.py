from fastapi import FastAPI
from pydantic import BaseModel
from chat import getresponse

app= FastAPI()


class Item(BaseModel):
       name:str


@app.get("/")
async def root():
       return ({"mesaage":"Hello"})

@app.post("/")
async def fun(item:Item):
       user_data = item.name
       response = getresponse(user_data)
       return({"message": response})




