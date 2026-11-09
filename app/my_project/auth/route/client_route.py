from flask import Blueprint
from app.my_project.auth.controller.client_controller import ClientController

client_bp = Blueprint('client_bp', __name__)
controller = ClientController()

client_bp.route('/', methods=['GET'])(controller.get_all)
client_bp.route('/<int:client_id>', methods=['GET'])(controller.get_by_id)
client_bp.route('/', methods=['POST'])(controller.create)
client_bp.route('/<int:client_id>', methods=['PUT'])(controller.update)
client_bp.route('/<int:client_id>', methods=['DELETE'])(controller.delete)
# Зв'язок 1:M (рахунки клієнта)
client_bp.route('/<int:client_id>/accounts', methods=['GET'])(controller.get_client_accounts)
client_bp.route('/<int:client_id>/providers', methods=['GET'])(controller.get_client_providers)