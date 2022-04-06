from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class BlackList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    app_id = db.Column(db.String(70))
    blocked_reason = db.Column(db.String(200))
    created_ts = db.Column(db.DateTime,  default=db.func.current_timestamp())
    ip_address = db.Column(db.String(50))

    __table_args__ = (
        db.UniqueConstraint('email', 'app_id',
                            name='unique_email_per_application'),
    )

    def __repr__(self):
        return "{} - {}".format(self.app_id, self.email)


class BlackListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BlackList
        include_relationships = True
        load_instance = True
