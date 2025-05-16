from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from enum import Enum
from datetime import datetime
from model.CounselPurposeAndNote import CounselPurposeAndNote

class CardRecordStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class Communications(str, Enum):
    WELL_COMMUNICATE = "WELL_COMMUNICATE"
    SEMI_COMMUNICATE = "SEMI_COMMUNICATE"
    NOT_COMMUNICATE = "NOT_COMMUNICATE"


class DrinkingAmount(str, Enum):
    NONE = "NONE"
    ONCE_A_WEEK = "ONCE_A_WEEK"
    TWICE_A_WEEK = "TWICE_A_WEEK"
    THREE_TIMES_A_WEEK = "THREE_TIMES_A_WEEK"
    FOUR_TIMES_A_WEEK = "FOUR_TIMES_A_WEEK"
    FIVE_OR_MORE_TIMES_A_WEEK = "FIVE_OR_MORE_TIMES_A_WEEK"


class ExercisePattern(str, Enum):
    NO_EXERCISE = "NO_EXERCISE"
    ONCE_A_WEEK = "ONCE_A_WEEK"
    TWICE_A_WEEK = "TWICE_A_WEEK"
    THREE_TIMES_A_WEEK = "THREE_TIMES_A_WEEK"
    FOUR_TIMES_A_WEEK = "FOUR_TIMES_A_WEEK"
    FIVE_OR_MORE_TIMES_A_WEEK = "FIVE_OR_MORE_TIMES_A_WEEK"


class MealPattern(str, Enum):
    ONE_REGULAR_MEAL = "ONE_REGULAR_MEAL"
    TWO_REGULAR_MEALS = "TWO_REGULAR_MEALS"
    THREE_REGULAR_MEALS = "THREE_REGULAR_MEALS"
    IRREGULAR_MEALS = "IRREGULAR_MEALS"


class SmokingAmount(str, Enum):
    NONE = "NONE"
    ONE_PACK = "ONE_PACK"
    TWO_PACKS = "TWO_PACKS"
    THREE_OR_MORE_PACKS = "THREE_OR_MORE_PACKS"


class WaterIntake(str, Enum):
    LESS_THAN_500ML = "LESS_THAN_500ML"
    BETWEEN_500ML_AND_1L = "BETWEEN_500ML_AND_1L"
    BETWEEN_1L_AND_1_5L = "BETWEEN_1L_AND_1_5L"
    BETWEEN_1_5L_AND_2L = "BETWEEN_1_5L_AND_2L"
    MORE_THAN_2L = "MORE_THAN_2L"


# --- 모델 정의 ---
class CounselCard(SQLModel, table=True):
    __tablename__ = "counsel_cards"

    id: str = Field(primary_key=True, max_length=26)
    created_by: Optional[str]
    created_datetime: Optional[datetime]
    updated_by: Optional[str]
    updated_datetime: Optional[datetime]
    is_allergic: Optional[bool]
    card_record_status: Optional[CardRecordStatus]
    communications: Optional[Communications]
    medication_note: Optional[str]
    significant_note: Optional[str]
    history_note: Optional[str]
    main_inconvenience_note: Optional[str]
    drinking_amount: Optional[DrinkingAmount]
    evacuation_note: Optional[str]
    exercise_note: Optional[str]
    exercise_pattern: Optional[ExercisePattern]
    house_mate_note: Optional[str]
    is_alone: Optional[bool]
    is_medication_side_effect: Optional[bool]
    meal_pattern: Optional[MealPattern]
    nutrition_note: Optional[str]
    smoking_amount: Optional[SmokingAmount]
    smoking_period_note: Optional[str]
    walking_note: Optional[str]
    allergy_note: Optional[str]
    suspected_medication_note: Optional[str]
    symptoms_note: Optional[str]
    custom_medication_assistant: Optional[str]
    water_intake: Optional[WaterIntake]
    counsel_session_id: str = Field(nullable=False, foreign_key="counsel_sessions.id")
    counsel_purpose_and_notes: List[CounselPurposeAndNote] = Relationship(back_populates=None)
