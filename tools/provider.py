import uuid


class provider:
    def guid(self) -> str:
        return str(uuid.uuid4()).upper()
