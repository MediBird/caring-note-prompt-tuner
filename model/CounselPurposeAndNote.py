from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

class CounselPurposeType(str, Enum):
    MEDICATION_SIDE_EFFECT = "MEDICATION_SIDE_EFFECT" ##약물 부작용 상담
    LIFESTYLE_MANAGEMENT = "LIFESTYLE_MANAGEMENT" ##생활습관 관리
    SYMPTOM_DISEASE_UNDERSTANDING = "SYMPTOM_DISEASE_UNDERSTANDING" ##증상/질병에 대한 이해
    MEDICATION_REVIEW = "MEDICATION_REVIEW" ##복용약물에 대한 검토
    OTHER = "OTHER" ##기타


class CounselPurposeAndNote(SQLModel, table=True):
    __tablename__ = "counsel_purpose"

    counsel_purpose_and_note_id: str = Field(foreign_key="counsel_cards.id", nullable=False, primary_key=True)
    counsel_purpose: CounselPurposeType = Field(nullable=False, primary_key=True)

