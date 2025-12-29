import datetime

from fastapi import Request, FastAPI, APIRouter

app = FastAPI(title="Assistente WhatsApp")

# router = APIRouter(prefix="/webhook")
# app.include_router(router)

@app.post("/webhook")
async def catch_all(path: str, request: Request):
    body = await request.body()
    headers = dict(request.headers)

    print("==== NOVO WEBHOOK ====")
    print("Path:", path)
    print("Headers:", headers)
    print("Body:", body.decode())

    return {
        "status": "received",
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/webhook")
async def webhook(request: Request):
    body = await request.body()
    print("==== NOVO WEBHOOK ====")
    print("Path:", body)
    print("Headers:", request.headers)
    print("Body:", body.decode())
    return {}
