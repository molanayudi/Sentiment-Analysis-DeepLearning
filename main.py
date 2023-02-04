from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from routes import analytics, cleansing

app = FastAPI()

@app.get("/version")
async def index():
    return JSONResponse(
        content = {
            "ok": True,
            "code": 200,
            "data": {"version": "1.0.0"},
            "messege": "Success"
        }
    )
    


app.include_router(analytics.router, tags=["Analytics"])
app.include_router(cleansing.router, tags=["Cleansing"])