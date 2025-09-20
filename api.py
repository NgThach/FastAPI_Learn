from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello(): 
    return {"Hello World"}

@app.get("/want")
def what_do_you_want(): 
    return {"What do you want"}

class Item(BaseModel):
    name: str
    price: float 
    
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}

@app.put("/add")
def create(mailbox: Item):
    return {"name_mail": mailbox.name, "price": mailbox.price}