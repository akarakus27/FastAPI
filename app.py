import uvicorn
from fastapi import FastAPI, Header

app = FastAPI ()
"""
@app.get('/')
async def rootI():
    return {"message": "Hello World"}

@app.get('/giris')
async def rootI():
    return {"key": "hatalı giris"}


@app.get('/')
async def root():
    num1= 4
    num2= 3
    result= num2*num1

    return {"Result": result}

@app.get('/items/{item_id}')
async def read_item(item_id):
    return {"item_id": item_id}
"""
@app.get('/items/{item_id}')
async def read_item(item_id:int):
    return {"item_id": item_id}

@app.get('/users/me')
async def read_user_me():
    return {"user_id": "the current user"}

@app.get('/users/{user_id}')
async def read_user_me(user_id:str):
    return {"user_id": user_id}

#buraso ayrı bir yer
from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/model{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.aalexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN "}

    return {"model_name": model_name, "message": "Have some residuals"}



#burası ayrı

from fastapi import FastAPI
from typing import Union


app = FastAPI()


#fake_item_db =[{"item_name":"Foo"},{"item_name":"Bar"}]
#@app.get("/items")
#async def read_item(skip: int=0 ,limit: int=10):
#    return fake_item_db[skip: skip+limit]


#@app.get('/items/{item_id}')
#async def read_item(item_id:str ,q:Union[str:None]=None):
#    if q:
#        return {"item_id": item_id,"q":q}
#    return {"item_id": item_id}

@app.get('/items/{item_id}')
async def read_user_item(item_id:str ,needy:str):
    item = {"item_id": item_id,"needy": needy,}
    return item



@app.get('/items')
async def read_items(user_agent: Union[str,None] = Header(default=None)):
    return {"User-Agent":user_agent}

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    description :Union[str,None]=None
    price: float
    tax:Union[float,None]=None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# burasın düzenle




