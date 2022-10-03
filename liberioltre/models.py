import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120))
    accentColor = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    options = db.relationship("Option", back_populates="product")

    def __repr__(self):
        return "<Product %r>" % self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    product = db.relationship("Product")

    def __repr__(self):
        return "<Option %r>" % self.option

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120))

    def __repr__(self):
        return "<User %r>" % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(16))
    option_id = db.Column(db.Integer, db.ForeignKey("option.id"))
    option = db.relationship("Option")
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Cart %r>" % self.option

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coupon = db.Column(db.String(64))
    discount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Coupon %r>" % self.coupon

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Customer(db.Model):
    # phone ed email sono nullable in attesa di implementare un remember me
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    firstName = db.Column(db.String(64), nullable=False)
    lastName = db.Column(db.String(64), nullable=False)
    street = db.Column(db.String(64), nullable=False)
    appartment = db.Column(db.String(64), nullable=False)
    postalCode = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    province = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "<Customer %r>" % self.email

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


association_table = db.Table(
    "orderDetails",
    db.Column("orderId", db.ForeignKey("order.id")),
    db.Column("optionId", db.ForeignKey("option.id")),
)


class Order(db.Model):
    # phone ed email sono nullable in attesa di implementare un remember me
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), nullable=False)
    paymentIntent = db.Column(db.String(80))
    shippingMode = db.Column(db.String(64))
    status = db.Column(db.String(64))
    additionalNotes = db.Column(db.String(64))
    shippedAt = db.Column(db.DateTime)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    details = db.relationship("Option", secondary=association_table)
    couponId = db.Column(db.Integer, db.ForeignKey("coupon.id"))
    customer = db.relationship("Customer")
    customerId = db.Column(db.Integer, db.ForeignKey("customer.id"))
    coupon = db.relationship("Coupon")
    total = db.Column(db.Float)
    subtotal = db.Column(db.Float)

    def __repr__(self):
        return "<Order %r>" % self.slug

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}