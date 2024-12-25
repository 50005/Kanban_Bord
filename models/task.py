from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, nullable=False, default="В очереди")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    project_id = Column(Integer, ForeignKey('project.id'))
    column_id = Column(Integer, ForeignKey('column.id'))

    project = relationship("Project", back_populates="tasks")
    column = relationship("ColumnModel", back_populates="tasks")
    logs = relationship("Log", back_populates="task", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Task id={self.id}, title='{self.title}'>"