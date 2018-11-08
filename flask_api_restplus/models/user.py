from .. import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # Additional fields

    def __repr__(self):
        return 'User {}>'.format(self.id)
