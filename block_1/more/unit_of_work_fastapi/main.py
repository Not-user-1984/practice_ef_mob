from fastapi import FastAPI, HTTPException
from unit_of_work import UnitOfWork
from schemas import UserCreate, UserResponse
from init_db import init_db

app = FastAPI()

init_db()


@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    with UnitOfWork() as uow:
        new_user = uow.user_repository.create_user(user)
        uow.commit()
        return new_user


@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    with UnitOfWork() as uow:
        user = uow.user_repository.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user


import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
