from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

from datetime import datetime

Base = declarative_base()

class NutritionReports(Base):
    __tablename__ = "nutrition_reports"

    id = Column(Integer, primary_key=True)

    current_weight = Column(Float, nullable=False)

    goal_weight = Column(Float, nullable=False)

    calories = Column(Float, nullable=False)

    protein = Column(Float, nullable=False)

    fat = Column(Float, nullable=False)

    fiber = Column(Float, nullable=False)

    carbohydrates = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
