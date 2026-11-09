from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(13), nullable=False, unique=True)
    id_code = db.Column(db.String(20), nullable=False, unique=True)

    # Зв'язок 1:M з рахунками
    accounts = db.relationship('Account', backref='client', lazy=True, cascade="all, delete")
    templates = db.relationship('SavedTemplate', backref='client', lazy=True, cascade="all, delete")
    def put_into_dto(self) -> dict:
        """Перетворення моделі в DTO (словник/JSON)"""
        return {
            'id': self.id,
            'client_name': self.client_name,
            'phone': self.phone,
            'id_code': self.id_code
        }

    @staticmethod
    def create_from_dto(dto_dict: dict):
        """Створення об'єкта моделі з отриманого DTO"""
        return Client(
            client_name=dto_dict.get('client_name'),
            phone=dto_dict.get('phone'),
            id_code=dto_dict.get('id_code')
        )