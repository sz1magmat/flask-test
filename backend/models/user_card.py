from models import db

class UserCard(db.Model):
    id = db.Column(
        db.SmallInteger,
        unique=True,
        nullable=False,
        primary_key=True,
        autoincrement=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        unique=True,
        nullable=False,
        primary_key=False,
        autoincrement=False)

    card_id = db.Column(
        db.SmallInteger,
        db.ForeignKey("card.id"),
        unique=True,
        nullable=False,
        primary_key=False,
        autoincrement=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "card_id": self.card_id}