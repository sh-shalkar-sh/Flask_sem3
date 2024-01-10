# Модели
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

# создаётся экземпляр
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)  # метод преобразует пароль в набор хеш символов

    def check_password(self, password):
        return check_password_hash(self.password, password) # данный метот получает и сравнивает хеш символы


