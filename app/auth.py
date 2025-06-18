from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.utils import hash_password, verify_password, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(name: str, email: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter_by(email=email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    user = User(name=name, email=email, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    return {"message": "Usuário registrado"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
