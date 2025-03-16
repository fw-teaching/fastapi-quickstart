import uvicorn
from fastapi import FastAPI

PORT=5000

app = FastAPI()

@app.get("/")
def hello():
    return { "message": "Hello FastAPI" }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",
        ssl_certfile="/etc/letsencrypt/fullchain.pem",
    )
