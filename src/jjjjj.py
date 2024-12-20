from fastapi import FastAPI

app = FastAPI()

@app.get("/ggg")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}