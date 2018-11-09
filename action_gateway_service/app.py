import os

from sanic import Sanic
from sanic.response import json


SPIDER_RUNTIME_STAGE = os.environ['SPIDER_RUNTIME_STAGE']


app = Sanic(__name__)


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000,
            debug=(SPIDER_RUNTIME_STAGE in ('feature', 'develop')))
