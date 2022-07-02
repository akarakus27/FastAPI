from typing import Union,List,Set
from fastapi import FastAPI,Form,File,UploadFile,HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name:str
    description : Union[str:None]=None
    price :float
    tax :Union[str,None]=None
    tags :Set[str]=set()


@app.post("/item/",response_model=Item,tags=["items"])
async def create_item (item:Item):
    return Item

@app.get("/items/",tags=["items"])
async def read_item():
    return[{"name":"Foo","Price":50}]

@app.get("//users",tags=["users"])
async def read_users():
    return [{"usernam":"johndoe"}]