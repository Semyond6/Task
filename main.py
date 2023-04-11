from fastapi import FastAPI, Body
from redis_om import NotFoundError

from models import UserData

app = FastAPI()


@app.get('/check_data')
async def check_data(phone: str):
    try:
        result = UserData.get(phone)
    except NotFoundError:
        result = {'error': 'No resource found'}

    return result


@app.post('/write_data')
async def write_data(
    data=Body(
        ...,
        example={
            'phone': '89993334444',
            'address': 'г.Москва, 3-я улица Строителей, д. 25, кв. 12',
        }
    ), ):

    try:
        user_data = UserData.get(data['phone'])
    except NotFoundError:
        user_data = None

    if user_data:
        user_data.update(
            **data
        )
    else:
        user_data = UserData(**data)
        user_data.save()
    result = user_data
    return {'success': str(result)}
