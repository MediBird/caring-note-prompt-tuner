from sqlmodel import create_engine, Session, select
from dotenv import load_dotenv
import os
from model.AICounselSummary import AICounselSummary
from model.MedicationCounsel import MedicationCounsel
from model.CounselSession import CounselSession, ScheduleStatus
import pandas as pd
from datetime import datetime

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)


def get_counsel_sessions(start_datetime: datetime, end_datetime: datetime = datetime.now()):
    with Session(engine) as session:
        result = session.exec(select(CounselSession)
                              .where(CounselSession.scheduled_start_datetime >= start_datetime)
                              .where(CounselSession.scheduled_start_datetime <= end_datetime)
                              .where(CounselSession.status == ScheduleStatus.COMPLETED), execution_options={"prebuffer_rows": True})

        return pd.DataFrame([r.model_dump() for r in result])

def get_summaries():
    with Session(engine) as session:
        result = session.exec(select(AICounselSummary)).all()
        return pd.DataFrame([r.dict() for r in result])


df = get_counsel_sessions(start_datetime=datetime.strptime("2025-04-01 00:00", "%Y-%m-%d %H:%M"))
print(df.count())