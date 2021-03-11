from fastapi import FastAPI
from app.services.messages_service import MessageService

app = FastAPI()


@app.get('/', status_code=200)
def get_goog_vibes():
    return f'Welcome!'


@app.get('/good', status_code=200)
def get_goog_vibes():
    return MessageService().get_good_vibe_message()


@app.get('/bad', status_code=200)
def get_bad_vibes():
    return MessageService().get_bad_vibe_message()
