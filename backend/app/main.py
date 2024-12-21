from fastapi import FastAPI, UploadFile, Form
from app.database import get_db
from app.models import Video
from app.crud import create_video, fetch_videos
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/upload_video/")
async def upload_video(
    file: UploadFile, title: str = Form(...), description: str = Form(...), db: Session = next(get_db())
):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return create_video(db, title, description, file_path)

@app.get("/fetch_videos/")
def fetch_all_videos(db: Session = next(get_db())):
    return fetch_videos(db)
