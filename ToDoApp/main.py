from fastapi import FastAPI
from .routers import auth, todos, admin, users
from .models import Base
from .database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
