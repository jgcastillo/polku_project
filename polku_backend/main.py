from fastapi import FastAPI

from polku_backend.shared.logger import logger

app = FastAPI()

@app.get("/")
async def healthcheck():
    logger.info("probando el logger")
    return {"message": "Polku backend working"}