from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority:int = Field(gt=0, lt=6, description="the priority is must between 1-5")
    complete :bool




@app.get("/")
def read_all(db: Session = Depends(get_db)):
    return  db.query(models.Todos).all()

@app.post("/")
def create_todo(todo : Todo, db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description= todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    db.add(todo_model) #this add places an object in the session for next flush operaton
    db.commit()
    return succesful_response(201)

@app.put("/{todo_id}")
def update_todo(todo_id : int , todo : Todo, db : Session = Depends(get_db)):
    todo_model = db.query(models.Todos) \
    .filter(models.Todos.id == todo_id) \
    .first()
    if todo_model is None:
        raise http_exception()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()
    return succesful_response(201)



@app.delete("/{todo_id}")
def delete_todo(todo_id : int ,db:Session = Depends(get_db)):
    todo_model = db.query(models.Todos) \
    .filter(models.Todos.id == todo_id) \
    .first()

    if todo_model is None:
        raise http_exception()
    db.query(models.Todos)\
    .filter(models.Todos.id == todo_id)\
    .delete()

    db.commit()
    return succesful_response(200)
def succesful_response(status_code : int ):
    return {
        'status': status_code,
        'transaction': 'successful'
    }








@app.get("/todo/{todo_id}")
def read_todo(todo_id : int, db: Session = Depends(get_db)): #depends is for dependency
    todo_model = db.query(models.Todos) \
    .filter(models.Todos.id ==todo_id) \
    .first()
    #filter allows to filter our sql command to navigate records with in a table
    if todo_model is not None:
        return todo_model
    raise http_exception()


def http_exception():
    return HTTPException(status_code=404, detail="not found")