from werkzeug.security import generate_password_hash, check_password_hash
from src.database import db
import bcrypt


"""
Defining user model schema
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    mobile_no = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False, default='user')
    is_verified = db.Column(db.Boolean, default=False)
  

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, password, hashed):
        return bcrypt.checkpw(password.encode(), hashed.encode())
