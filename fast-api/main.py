from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
  attributes = {
    "First Name": "Sophie",
    "Surname": "Muriel",
    "Age": 20,
    "Favourite Colour": "yellow",
    "Favourite Game": "Celeste"
  }
  return attributes