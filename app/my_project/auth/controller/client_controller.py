from http import HTTPStatus
from flask import jsonify, request
from app.my_project.auth.service.client_service import ClientService

class ClientController:
    def __init__(self):
        self.service = ClientService()

    def get_all(self):
        return jsonify(self.service.get_all_clients()), HTTPStatus.OK

    def get_by_id(self, client_id: int):
        client = self.service.get_client_by_id(client_id)
        if not client:
            return jsonify({'message': 'Клієнта не знайдено'}), HTTPStatus.NOT_FOUND
        return jsonify(client), HTTPStatus.OK

    def create(self):
        data = request.get_json()
        try:
            res = self.service.create_client(data)
            return jsonify(res), HTTPStatus.CREATED
        except ValueError as err:
            return jsonify({'error': str(err)}), HTTPStatus.BAD_REQUEST

    def update(self, client_id: int):
        data = request.get_json()
        res = self.service.update_client(client_id, data)
        if not res:
            return jsonify({'message': 'Клієнта не знайдено'}), HTTPStatus.NOT_FOUND
        return jsonify(res), HTTPStatus.OK

    def delete(self, client_id: int):
        success = self.service.delete_client(client_id)
        if not success:
            return jsonify({'message': 'Клієнта не знайдено'}), HTTPStatus.NOT_FOUND
        return jsonify({'message': 'Клієнта успішно видалено'}), HTTPStatus.OK

    def get_client_accounts(self, client_id: int):
        accounts = self.service.get_accounts_for_client(client_id)
        if accounts is None:
            return jsonify({'message': 'Клієнта не знайдено'}), HTTPStatus.NOT_FOUND
        return jsonify(accounts), HTTPStatus.OK
    def get_client_providers(self, client_id: int):
        providers = self.service.get_providers_for_client(client_id)
        if providers is None:
            return jsonify({'message': 'Клієнта не знайдено'}), HTTPStatus.NOT_FOUND
        return jsonify(providers), HTTPStatus.OK