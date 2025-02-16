from src.database import db
from datetime import datetime

"""
Defining product model schema
"""
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    cost_price = db.Column(db.Float, nullable=False)
    selling_price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    stock_available = db.Column(db.Integer, default=0)
    units_sold = db.Column(db.Integer, default=0)
    customer_rating = db.Column(db.Float)
    optimized_price = db.Column(db.Float)
    demand_forecast = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
