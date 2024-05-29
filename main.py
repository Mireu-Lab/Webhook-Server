from webhook import subscribeAdd, subscribeInfo

from fastapi import FastAPI
app = FastAPI()

@app.get("/subscribe_info")
async def subscribe_info():
    return subscribeInfo()


@app.get("/subscribe")
async def subscribe(URL: str, Type: bool):
    return subscribeAdd(URL, Type)

@app.get("/callback")
async def callback():
    print(subscribeInfo())

    pass