from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base
from models.base import project_user_association

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
    users = relationship("User", secondary=project_user_association, back_populates="projects")
    logs = relationship("Log", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project id={self.id}, title='{self.title}'>"