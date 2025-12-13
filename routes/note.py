# from fastapi import APIRouter
# from fastapi.responses import RedirectResponse
# from fastapi import FastAPI, Request
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from models.note import Note
# from config.db import conn 
# from schemas.note import noteEntity,notesEntity

# note = APIRouter()

# # note.mount("/static", StaticFiles(directory="static"), name="static")hjhjh
# templates = Jinja2Templates(directory="templates")

# @note.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     newDocs = []
#     docs = conn.notes.notes.find({})
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "note": doc["note"],
#             "desc":doc["desc"],
#             "important":doc["important"]
#         })
    
#     return templates.TemplateResponse(  
#         "index.html",
#         {"request": request, "newDocs": newDocs}
#     )



# # @note.post("/")
# # async def create_item(request:Request):
# #     form = await request.form()
# #     formDict = dict(form)
# #     formDict["important"] = True if formDict.get("important") == "on" else False
# #     note = conn.notes.notes.insert_one(formDict)
# #     return {"Success": True}


from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn

note = APIRouter()
templates = Jinja2Templates(directory="templates")


# ---------- GET ROUTE ----------
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    newDocs = []
    docs = conn.notes.notes.find({})
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "note": doc.get("note"),
            "desc": doc.get("desc"),
            "important": doc.get("important"),
        })

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "newDocs": newDocs}
    )


# ---------- POST ROUTE ----------
@note.post("/")
async def create_item(request: Request):
    form = await request.form()

    data = {
    "note": form.get("title"),   # FIXED NAME
    "desc": form.get("desc"),
    "important": form.get("important") == "on"
}


    conn.notes.notes.insert_one(data)

    # Correct redirect for your setup
    return RedirectResponse(url="/", status_code=303)













