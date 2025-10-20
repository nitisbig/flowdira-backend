from fastapi import FastAPI
from api.routes import user_route
from api.routes import auth_route

app = FastAPI()
app.include_router(user_route.router)
app.include_router(auth_route.router)

@app.get('/')
def root():
    return 'hello'

