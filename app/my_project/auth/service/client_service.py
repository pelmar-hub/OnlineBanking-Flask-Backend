from app.my_project.auth.dao.client_dao import ClientDAO
from app.my_project.auth.domain.client import Client

class ClientService:
    def __init__(self):
        self.dao = ClientDAO()

    def get_all_clients(self):
        clients = self.dao.find_all()
        return [client.put_into_dto() for client in clients]

    def get_client_by_id(self, client_id: int):
        client = self.dao.find_by_id(client_id)
        return client.put_into_dto() if client else None

    def create_client(self, client_dto: dict):
        # Бізнес-перевірка
        if not client_dto.get('phone') or not client_dto.get('id_code'):
            raise ValueError("Телефон та ІПН обов'язкові до заповнення")
        client = Client.create_from_dto(client_dto)
        created_client = self.dao.create(client)
        return created_client.put_into_dto()

    def update_client(self, client_id: int, client_dto: dict):
        updated = self.dao.update(client_id, client_dto)
        return updated.put_into_dto() if updated else None

    def delete_client(self, client_id: int):
        return self.dao.delete(client_id)

    def get_accounts_for_client(self, client_id: int):
        """Вимога завдання: вивід зі сторони зв'язку 1:M"""
        client = self.dao.find_by_id(client_id)
        if not client:
            return None
        return [acc.put_into_dto() for acc in client.accounts]
    def get_providers_for_client(self, client_id: int):
        client = self.dao.find_by_id(client_id)
        if not client:
            return None
        templates = self.dao.find_providers_by_client_id(client_id)
        return [t.put_into_dto() for t in templates]