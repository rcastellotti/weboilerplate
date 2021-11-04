from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from nanoid import generate
from flask_cors import CORS
import os

database = os.getenv("DB")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


class Signs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(8), unique=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.post("/api")
def add():
    print(request.json)
    message = request.json["message"]
    sign = Signs(message=message, slug=generate(size=8))
    db.session.add(sign)
    db.session.commit()
    return{"message": "sign created", "sign": sign.as_dict()}


@ app.get("/api/<slug>")
def get(slug):
    sign = Signs.query.filter_by(slug=slug).first()
    return sign.as_dict(), 200


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)
