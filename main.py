from fastapi import FastAPI
from api.routes import user_route

app = FastAPI()
app.include_router(user_route.router)

@app.get('/')
def root():
    return 'hello'

