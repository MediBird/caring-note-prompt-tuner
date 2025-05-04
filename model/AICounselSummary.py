from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, TYPE_CHECKING, List
from enum import Enum
from model.CounselSession import CounselSession
from model.decorator.JSONText import JSONText

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

    stt_result: Optional[dict] = Field(default=None, sa_column=Column(JSONText))
    ta_result: Optional[dict] = Field(default=None, sa_column=Column(JSONText))

    ai_counsel_summary_status: Optional[AICounselSummaryStatus] = Field(default=None)

    speakers: Optional[str] = Field(default=None)

    counsel_session: Optional["CounselSession"] = Relationship(back_populates="ai_counsel_summary")

    def get_ai_summary_result(self):
        if self.ta_result:
            return self.ta_result['result']['output']['text']

        return ''

    def get_stt_result(self) -> List[dict]:

        stt_results = List[dict]

        if self.stt_result:
            speakers = self.__get_speakers()
            stt_results = [
                {
                    'speaker': segment['speaker']['name'],
                    'text': segment['text']
                }
                for segment in self.stt_result['segments']
                if segment['speaker']['name'] in speakers
            ]

        return stt_results

    def __get_speakers(self) -> List[str]:
        return self.speakers.split("^=^")
