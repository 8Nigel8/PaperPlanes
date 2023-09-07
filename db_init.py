from settings import engine
from app.src.models import Base

Base.metadata.create_all(bind=engine)

