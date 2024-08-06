from .pydantic_models import ClientSessionCreate


class BuildObjects:
    def build_clients(self):
        pass

    def build_client_session(self, client_id: int, message_id: int) -> ClientSessionCreate:
        return ClientSessionCreate(
            client_id=client_id,
            message_id=message_id
        )

