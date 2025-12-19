from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/internships", response_model=schemas.InternshipResponse)
def create_internship(
    internship: schemas.InternshipCreate,
    db: Session = Depends(get_db)
):
    db_internship = models.Internship(**internship.dict())
    db.add(db_internship)
    db.commit()
    db.refresh(db_internship)
    return db_internship
@app.get("/internships", response_model=list[schemas.InternshipResponse])
def get_internships(db: Session = Depends(get_db)):
    return db.query(models.Internship).all()
