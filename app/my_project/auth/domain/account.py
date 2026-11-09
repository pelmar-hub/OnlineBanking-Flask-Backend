from app.my_project.auth.domain.client import db

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id', ondelete='CASCADE'), nullable=False)
    balance = db.Column(db.Numeric(15, 2), nullable=False, default=0.00)
    type_id = db.Column(db.Integer, nullable=False)
    currency_id = db.Column(db.Integer, nullable=False)

    def put_into_dto(self) -> dict:
        return {
            'id': self.id,
            'client_id': self.client_id,
            'balance': float(self.balance),
            'type_id': self.type_id,
            'currency_id': self.currency_id
        }