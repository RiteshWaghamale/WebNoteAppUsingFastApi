from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")



# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     newDocs = []
#     docs = conn.notes.notes.find({})
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#         })
    
#     return templates.TemplateResponse(
#         "index.html",
#         {"request": request, "newDocs": newDocs}
#     )



# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI!"}
