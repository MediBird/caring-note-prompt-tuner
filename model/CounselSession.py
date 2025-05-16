from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from enum import Enum

if TYPE_CHECKING:
    from model.AICounselSummary import AICounselSummary
    from model.MedicationCounsel import MedicationCounsel
    from model.CounselCard import CounselCard


class ScheduleStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"


class CounselSession(SQLModel, table=True):
    __tablename__ = "counsel_sessions"

    id: Optional[str] = Field(default=None, primary_key=True)

    # 외래 키만 사용 (조인 없이)
    counselor_id: Optional[str] = Field(default=None, foreign_key="counselor.id")
    counselee_id: Optional[str] = Field(default=None, foreign_key="counselee.id")

    scheduled_start_datetime: datetime
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None

    status: ScheduleStatus

    session_number: Optional[int] = None

    ai_counsel_summary: Optional["AICounselSummary"] = Relationship(back_populates="counsel_session")
    medication_counsel: Optional["MedicationCounsel"] = Relationship(back_populates="counsel_session")
    counsel_card: Optional["CounselCard"] = Relationship(back_populates=None)
