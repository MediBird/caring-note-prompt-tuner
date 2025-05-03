from sqlalchemy.types import TypeDecorator, TEXT
import json


class JSONText(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        return json.dumps(value) if value is not None else None

    def process_result_value(self, value, dialect):
        return json.loads(value) if value else None
