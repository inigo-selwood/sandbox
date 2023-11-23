import nltk
import fastapi

from . import endpoints


app = fastapi.FastAPI()


for router in endpoints.routers:
    app.include_router(router)
