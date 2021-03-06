import uvicorn

from app.main import FastAPI, app
from app.utils.logger import logger


class Coordinator:
    def __init__(self):
        self.app = FastAPI()

    def run(self):
        uvicorn.run(app, host='0.0.0.0')
        logger.info("Good Vibes Messages stoping...")
