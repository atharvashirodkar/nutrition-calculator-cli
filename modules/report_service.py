from database.db import SessionLocal
from database.models import NutritionReports


def create_report(data):
    session = SessionLocal()
    report = NutritionReports(**data)
    session.add(report)
    session.commit()
    session.refresh(report)
    session.close()


def get_all_reports():
    session = SessionLocal()
    reports = session.query(NutritionReports).all()
    session.close()
    return reports


def get_report_by_id(report_id):
    session = SessionLocal()
    report = (
        session.query(NutritionReports).filter(NutritionReports.id == report_id).first()
    )
    session.close()
    return report


def delete_report(report_id):
    session = SessionLocal()
    report = (
        session.query(NutritionReports).filter(NutritionReports.id == report_id).first()
    )
    if report:
        session.delete(report)
        session.commit()
        session.close()
        return True

    session.close()
    return False
