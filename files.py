from typing import Union,List
from fastapi import FastAPI,Form,File,UploadFile,HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(), fileb: UploadFile = File(), token: str = Form()):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type":fileb.content_type}


#items = {"foo": "The foo Wrestlers"}

#@app.get("/items/{item_id}")
#async def read_item(item_id :str):
#    if item_id not in items:
#        raise HTTPException(status_code=404 ,detail='Item not Found')
#    return {"item": items[item_id]}



@app.get("/redirection/")
async def redirect_url_not_found():
    return {"Welcome Home Page"}

items = {"foo": "The foo Wrestlers"}
@app.get("/items/{item_id}")
async def read_item(item_id: str ):
    if item_id not in items:
        return RedirectResponse('/redirection/',status_code=404)
    return {"items":item_id}


from typing import Union,List
from fastapi import FastAPI,Form,File,UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()
@app.post('/login/')
async def login(username: str = Form(), password: str= Form()):
    return {"username":username}

@app.post('/files/')
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

@app.post('/uploadfiles/')
async def create_upload(files:  List[UploadFile]):
    return {"filename": [file.filename for file in files]}


@app.get('/')
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files"type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/"
    enctype="multipart/form-data" method="post">
    <input name="files" type="file" 
    multiple><input type="submit">
    </form>
    </body>"""
    return HTMLResponse(content=content)