from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB section
DATABASE_URL = 'sqlite:///applicationData.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
