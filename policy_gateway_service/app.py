from sanic import Sanic
from policy_gateway_service.service.route import add_route

#SPIDER_RUNTIME_STAGE = os.environ['SPIDER_RUNTIME_STAGE']
SPIDER_RUNTIME_STAGE = 'feature'

app = Sanic(__name__)
if __name__ == "__main__":
#if __name__ == "app":
    add_route(app)
    app.run(host="0.0.0.0", port=8000,
            debug=(SPIDER_RUNTIME_STAGE in ('feature', 'develop')))
