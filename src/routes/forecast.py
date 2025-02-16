from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from src.models.product import Product

forecast_bp = Blueprint("forecast", __name__)

"""
path: /api/forecast/demand
method: POST
desc: endpoint to create the demand forecast of given products
"""
@forecast_bp.route("/demand", methods=["POST"])
@jwt_required()
def demand_forecast():

    data = request.json

#<--------------------------- method end --------------------------------------->