from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # store date and time in a string variable.
    datetime_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return {"message": "Hello World at {}".format(datetime_str)}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
