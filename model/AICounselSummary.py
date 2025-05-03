from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from enum import Enum
from model.CounselSession import CounselSession

if TYPE_CHECKING:
    from model.CounselSession import CounselSession
class AICounselSummaryStatus(str, Enum):
    STT_PROGRESS = "STT_PROGRESS"
    STT_COMPLETE = "STT_COMPLETE"
    GPT_PROGRESS = "GPT_PROGRESS"
    GPT_COMPLETE = "GPT_COMPLETE"


class AICounselSummary(SQLModel, table=True):
    __tablename__ = "ai_counsel_summarys"

    id: Optional[str] = Field(default=None, primary_key=True)

    counsel_session_id: str = Field(nullable=False, foreign_key="counsel_sessions.id")

    stt_result: Optional[str] = Field(default=None)
    ta_result: Optional[str] = Field(default=None)

    ai_counsel_summary_status: Optional[AICounselSummaryStatus] = Field(default=None)

    speakers: Optional[str] = Field(default=None)

    counsel_session: Optional["CounselSession"] = Relationship(back_populates="ai_counsel_summary")