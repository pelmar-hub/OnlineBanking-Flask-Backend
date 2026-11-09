from app.my_project.auth.domain.client import db

class SavedTemplate(db.Model):
    __tablename__ = 'saved_templates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id', ondelete='CASCADE'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('service_providers.id', ondelete='CASCADE'), nullable=False)
    template_name = db.Column(db.String(100), nullable=False)

    # Зв'язок із сутністю ServiceProvider для швидкого отримання даних
    provider = db.relationship('ServiceProvider', backref='templates', lazy=True)

    def put_into_dto(self) -> dict:
        return {
            'template_id': self.id,
            'template_name': self.template_name,
            'client_id': self.client_id,
            'provider': self.provider.put_into_dto() if self.provider else None
        }