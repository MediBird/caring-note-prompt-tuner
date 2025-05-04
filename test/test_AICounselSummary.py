import pytest
from model.AICounselSummary import AICounselSummary, AICounselSummaryStatus
from model.MedicationCounsel import MedicationCounsel
from model.CounselSession import CounselSession

@pytest.fixture
def dummy_summary():
    return AICounselSummary(
        id="test-id",
        counsel_session_id="session-id",
        stt_result={
            "segments": [
                {"speaker": {"name": "A"}, "text": "안녕하세요."},
                {"speaker": {"name": "B"}, "text": "약은 하루에 두 번 드세요."},
                {"speaker": {"name": "C"}, "text": "감사합니다."}
            ]
        },
        ta_result={
            "result": {
                "output": {
                    "text": "환자에게 하루 두 번 복용하도록 안내함."
                }
            }
        },
        ai_counsel_summary_status=AICounselSummaryStatus.GPT_COMPLETE,
        speakers="A^=^B"
    )


def test_get_ai_summary_result(dummy_summary):
    result = dummy_summary.get_ai_summary_result()
    assert result == "환자에게 하루 두 번 복용하도록 안내함."


def test_get_stt_result(dummy_summary):
    stt_results = dummy_summary.get_stt_result()
    assert len(stt_results) == 2
    assert stt_results[0]['speaker'] == 'A'
    assert stt_results[1]['speaker'] == 'B'


def test_get_speakers(dummy_summary):
    speakers = dummy_summary._AICounselSummary__get_speakers()
    assert speakers == ["A", "B"]