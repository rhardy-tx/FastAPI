#To test this program
#run main.py
#then from terminal start uvicorn:
#uvicorn main:APIapp --reload

from fastapi import FastAPI
import random

APIapp = FastAPI()



@APIapp.get("/lotto")
async def get_lotto():
    lotto = random.sample(range(1, 69), 5)
    str_lotto = ','.join(str(e) for e in lotto)
    str_message = "Your random lotto numbers are:\n" + str_lotto
    return {"message": str_message}

@APIapp.get("/powerball")
async def get_powerball():
    lotto = random.sample(range(1, 69), 5)
    str_lotto = ','.join(str(e) for e in lotto)
    powerball = str(random.randint(1, 26))
    return {"message": "Your new random lotto numbers are:" + str_lotto + ' with Powerball# ' + powerball}