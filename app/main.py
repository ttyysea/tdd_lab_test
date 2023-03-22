from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "World"}


@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname")
def post_call_name(name = "Jack"):
    return {"hello": name}


handler = Mangum(app)
