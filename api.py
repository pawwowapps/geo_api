from typing import Union
from fastapi import FastAPI
from model.models import *
from dotenv import load_dotenv
import telebot
import os

load_dotenv()

debug = os.getenv("DEBUG")
# telegram_token = os.getenv("TELEGRAM_TOKEN_DEBUG") if debug else os.getenv("TELEGRAM_TOKEN")
telegram_token = '6953404835:AAGh27UXqujVsvAixAZV7zuWBUwAU4n9p44'
user_token = os.getenv("USER_TOKEN")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/updateItem/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post('/predict')
def predict(age, sex, bmi, children, smoker, region):
    return 'Hello'




# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=10000)
