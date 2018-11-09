from sanic import response
from sanic.response import json
from .settings import API_VERSION
from .datasource import insert_policy_into_db
from .validation import validate_create_task


async def test(request):
    return json({"hello": "world"})

async def create_task(request):
    if not validate_create_task(request):
        return response.json(
            {'message': 'Wrong Format!'},
            status=400
        )
    task_id, created_time = insert_policy_into_db(request)
    return json({
        '_id': task_id,
        '_created': created_time
    })

def add_route(app):
    app.add_route(test, '/', methods=['GET'])
    app.add_route(create_task, '/' + API_VERSION + '/tasks', methods=['POST'])