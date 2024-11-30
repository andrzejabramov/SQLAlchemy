import uvicorn
from fastapi import FastAPI
from app.routers import category, products
from app.backend.db import engine, Base


app = FastAPI()


@app.get("/", summary="Главная ручка", tags=["Основные ручки"])
async def welcome():
    return {'message': 'My shop'}

app.include_router(category.router)
app.include_router(products.router)

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app")