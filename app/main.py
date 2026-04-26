from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {
        "item_id": item_id,
        "query": q
    }

@app.get("/hello")
def hello():
    return {"msg": "hello git practice !!!"}

@app.get("/test")
def test():
    return {"msg": "test git practice !!! !!!"}

@app.get("/test2")
def test2():
    return {"msg": "test2 git practice !!! !!! !!!"}

@app.get("/test3")
def test3():
    return {"msg": "test3 git practice !!! !!! !!! !!!"}