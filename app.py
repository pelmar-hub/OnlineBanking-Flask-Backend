import yaml
from flask import Flask
from app.my_project.auth.domain.client import db, Client
from app.my_project.auth.domain.account import Account 
from app.my_project.auth.route.client_route import client_bp
from app.my_project.auth.domain.service_provider import ServiceProvider
from app.my_project.auth.domain.saved_template import SavedTemplate
def create_app():
    app = Flask(__name__)

    # Зчитування YAML конфігурації
    with open('app/config/app.yml', 'r', encoding='utf-8') as f:
        config_data = yaml.safe_load(f)['db']

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{config_data['user']}:{config_data['password']}@"
        f"{config_data['host']}:{config_data['port']}/{config_data['database']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Реєстрація Blueprint-роутів
    app.register_blueprint(client_bp, url_prefix='/api/clients')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)