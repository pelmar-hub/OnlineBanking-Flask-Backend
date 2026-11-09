from app.my_project.auth.domain.client import Client, db

class ClientDAO:
    @staticmethod
    def find_all():
        return Client.query.all()

    @staticmethod
    def find_by_id(client_id: int):
        return Client.query.get(client_id)

    @staticmethod
    def create(client: Client):
        db.session.add(client)
        db.session.commit()
        return client

    @staticmethod
    def update(client_id: int, client_data: dict):
        client = Client.query.get(client_id)
        if client:
            client.client_name = client_data.get('client_name', client.client_name)
            client.phone = client_data.get('phone', client.phone)
            client.id_code = client_data.get('id_code', client.id_code)
            db.session.commit()
        return client

    @staticmethod
    def delete(client_id: int):
        client = Client.query.get(client_id)
        if client:
            db.session.delete(client)
            db.session.commit()
            return True
        return False
    @staticmethod
    def find_providers_by_client_id(client_id: int):
        from app.my_project.auth.domain.saved_template import SavedTemplate
        return SavedTemplate.query.filter_by(client_id=client_id).all()