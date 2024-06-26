from fastapi import Depends, HTTPException, Path, APIRouter
from fastapi.responses import JSONResponse
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session 
from pydantic import BaseModel, Field
from ..models import Todos
from ..database import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix = '/todos', 
    tags = ['to-dos']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_db)]
user_dependecy  = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_todos(user: user_dependecy, db: db_dependecy): 
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is required')
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo_by_id(user: user_dependecy, 
                    db : db_dependecy, 
                    todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is required')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='To-Do not found.')


@router.get("/completed", status_code=status.HTTP_200_OK)
async def read_completed_todos(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication is required")
    
    completed_todos = db.query(Todos).filter(Todos.owner_id == user.get('id'), Todos.complete == True).all()
    return completed_todos


@router.get("/priority/{priority}", status_code=status.HTTP_200_OK)
async def read_todos_by_priority(priority: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication is required")
    
    todos_by_priority = db.query(Todos).filter(Todos.owner_id == user.get('id'), Todos.priority == priority).all()
    return todos_by_priority


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependecy, 
                      db: db_dependecy, 
                      todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is required')
    todo_model = Todos(**todo_request.model_dump(), owner_id = user.get('id'))

    db.add(todo_model)
    db.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "To-Do Created successfully!"})


@router.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(user: user_dependecy,
                      db: db_dependecy, 
                      todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is required')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='To-Do not found.')
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "To-Do Updated successfully!"})


@router.delete("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(user: user_dependecy, 
                      db: db_dependecy, 
                      todo_id: int = Path(gt=0)):
    if todo_model is None:
        raise HTTPException(status_code=404, detail='To-Do not found.')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='To-Do not found')
    db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).delete()

    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "To-Do Deleted successfully!"})

