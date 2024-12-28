from fastapi import FastAPI
app=FastAPI()   


from routes.route import router


app.include_router(router)