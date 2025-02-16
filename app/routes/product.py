from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.product import Product
from app.database import db
from app.utils.helpers import create_unique_id

product_bp = Blueprint("product", __name__)


"""
path: /api/products
method: POST
desc: endpoint to create new product
"""
@product_bp.route("/", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    product = Product(
        product_id=create_unique_id(),
        name=data["name"],
        description=data["description"],
        cost_price=data["cost_price"],
        selling_price=data["selling_price"],
        category=data["category"],
        stock_available=data["stock_available"],
        units_sold=data["units_sold"],
        customer_rating=0,
        optimized_price=0,
        demand_forecast=0,
    )
    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product created successfully"}), 201

#<--------------------------- method end --------------------------------------->

"""
path: /api/products/:product_id
method: PUT
desc: endpoint to update the product details
"""
@product_bp.route("/<int:product_id>", methods=["PUT"])
@jwt_required()
def update_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()

    if "name" in data:
        product.name = data["name"]
    if "description" in data:
        product.description = data.get("description", product.description)
    if "cost_price" in data:
        product.cost_price = data["cost_price"]
    if "selling_price" in data:
        product.selling_price = data["selling_price"]
    if "stock_available" in data:
        product.stock_available = data["stock_available"]
    if "units_sold" in data:
        product.units_sold = data["units_sold"]
    if "customer_rating" in data:
        product.customer_rating = data["customer_rating"]
    if "demand_forecast" in data:
        product.demand_forecast = data["demand_forecast"]
    if "optimized_price" in data:
        product.optimized_price = data["optimized_price"]

    try:
        db.session.commit()
        return jsonify({"message": "Product updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error updating product", "error": str(e)}), 500

#<--------------------------- method end --------------------------------------->

"""
path: /api/products/:product_id
method: GET
desc: endpoint to get product detail by product id
"""
@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"message": "Product not found"}), 404

    product_details = {
        "product_id": product.product_id,
        "name": product.name,
        "description": product.description,
        "cost_price": product.cost_price,
        "selling_price": product.selling_price,
        "stock_available": product.stock_available,
        "units_sold": product.units_sold,
        "customer_rating": product.customer_rating,
        "demand_forecast": product.demand_forecast,
        "optimized_price": product.optimized_price,
        "category": product.category,
    }

    return jsonify(product_details), 200

#<--------------------------- method end --------------------------------------->

"""
path: /api/products/:product_id
method: DELETE
desc: endpoint to delete product by product id
"""
@product_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"message": "Product not found"}), 404

    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error deleting product", "error": str(e)}), 500

#<--------------------------- method end --------------------------------------->

"""
path: /api/products
method: GET
desc: endpoint to get all list of products
"""
@product_bp.route("/", methods=["GET"])
@jwt_required()
def get_products():
    query = Product.query
    # Search by name
    if "name" in request.args:
        search = request.args.get("name")
        query = query.filter(Product.name.ilike(f"%{search}%"))

    # Filter by category
    if "category" in request.args:
        category = request.args.get("category")
        if category != "All":
            query = query.filter_by(category=category)

    if "order_by" in request.args:
        print("inside the order by", request.args.get("order_by"))
        order_field = request.args.get("order_by")
        if order_field == "name":
            query = query.order_by(Product.name)
        elif order_field == "price":
            query = query.order_by(Product.price)

    products = query.all()
    return (
        jsonify(
            [
                {
                    "id": p.product_id,
                    "name": p.name,
                    "description": p.description,
                    "cost_price": p.cost_price,
                    "selling_price": p.selling_price,
                    "category": p.category,
                    "stock_available": p.stock_available,
                    "units_sold": p.units_sold,
                    "customer_rating": p.customer_rating,
                    "optimized_price": p.optimized_price,
                    "demand_forecast": p.demand_forecast,
                }
                for p in products
            ]
        ),
        200,
    )

#<--------------------------- method end --------------------------------------->