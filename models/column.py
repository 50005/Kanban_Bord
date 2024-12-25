from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base # Убираем импорт из models

class Column(Base):
    __tablename__ = "column"

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    project_id = Column(Integer(), ForeignKey('project.id'))
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    project = relationship("Project", back_populates="columns")
    tasks = relationship("Task", back_populates="column", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Column id={self.id}, title='{self.title}'>"