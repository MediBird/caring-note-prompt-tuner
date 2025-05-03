from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, TYPE_CHECKING, List
from model.decorator.JSONText import JSONText

if TYPE_CHECKING:
    from model.CounselSession import CounselSession

class MedicationCounsel(SQLModel, table=True):
    __tablename__ = "medication_counsels"

    id: Optional[str] = Field(default=None, primary_key=True)

    # CounselSession과 1:1 관계 - 조회만 할 것이므로 외래키 ID만 둠
    counsel_session_id: str = Field(nullable=False, foreign_key="counsel_sessions.id")

    # 중재 기록 (약사가 작성한 상담 텍스트)
    counsel_record: Optional[dict] = Field(
        default=None,
        sa_column=Column(JSONText)
    )

    counsel_session: Optional["CounselSession"] = Relationship(back_populates="medication_counsel")

    def get_full_counsel_record(self) -> str:
        if self.counsel_record[0]:
            children: List[dict] = self.counsel_record[0].get('children', [])
            joined = '\n'.join(
                f"**{d['text']}**" if d.get('bold') is True else d['text']
                for d in children if 'text' in d
            )
            return joined
        else:
            return ''

    def get_bold_text_in_counsel_record(self) -> list:

        bold_text_list = []

        if self.counsel_record[0]:
            children: List[dict] = self.counsel_record[0].get('children')
            bold_text_list = [item['text'] for item in children if item.get('bold') is True]

        return bold_text_list
