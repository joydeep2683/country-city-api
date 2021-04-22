from fastapi import FastAPI
from pydantic import BaseModel
from city_and_country import CountryWithCity


app = FastAPI()
country_city = CountryWithCity()


class Message(BaseModel):
    request : str

@app.post("/message/city/")
def get_only_city(message: Message):
    return country_city.get_city(message.request)

@app.post("/message/country/")
def get_only_country(message: Message):
    return country_city.get_country(message.request)

@app.post("/message/country_by_city/")
def get_country_by_city(message: Message):
    return country_city.get_country_by_city(message.request)
