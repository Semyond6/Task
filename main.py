from fastapi import FastAPI, Body
from redis_om import NotFoundError

from models import UserData
from typing import Dict
import os

os.environ["REDIS_OM_URL"]="redis://localhost:6379/0"
app = FastAPI()



@app.post('/write_data')
async def write_data(
    data=Body(
        ...,
        #regex=r'\+\d{1,15}',
        example={
            'phone': '+7111111111',
            'address': 'г.Москва, 3-я улица Строителей, д. 25, кв. 12',
        }
    ),) -> Dict[str, str]:

    user_data = None # UserData.find(
    #    UserData.phone == data['phone']
    #).all()
    if user_data:
        user_data.update(
            **data
        )
    else:
        user_data = UserData(phone = data['phone'], address = data['address'])
        user_data.save()

    result = user_data
    return {'success': bool(result)}



@app.get('/get_add_data')
async def get_all_data():
    result = {}
    try:
        result = UserData.all.all(), 200
    except NotFoundError:
        result = {'error': 'No resource found'}, 404

    return result
