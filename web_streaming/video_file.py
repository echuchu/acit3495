from base import Base
from sqlalchemy import Column, Integer, String

# Define the SQLAlchemy model for the table
class VideoFile(Base):
    __tablename__ = 'video_files'
    id = Column(Integer, primary_key=True)
    filename = Column(String(255))
    filepath = Column(String(255))