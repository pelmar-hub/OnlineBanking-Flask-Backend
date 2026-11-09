from app.my_project.auth.domain.client import db

class ServiceProvider(db.Model):
    __tablename__ = 'service_providers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(100), nullable=False)
    iban_account = db.Column(db.String(34), nullable=False)

    def put_into_dto(self) -> dict:
        return {
            'id': self.id,
            'company_name': self.company_name,
            'iban_account': self.iban_account
        }