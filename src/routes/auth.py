from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from src.models.user import User
from src.database import db
from flask_cors import cross_origin

auth_bp = Blueprint("auth", __name__)

"""
path: /api/auth/register
method: POST
desc: endpoint to create the user accounts
"""
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400

    try:
        user = User(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            mobile_no=data["mobile_no"],
        )
        user.set_password(data["password"])

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=user.id)

        return (
            jsonify(
                {
                    "message": "User registered successfully",
                    "access_token": access_token,
                    "user_id": user.id,
                }
            ),
            201,
        )
    except Exception as e:
        return jsonify({"message": "server internal error", "status": 500}), 500

#<--------------------------- method end --------------------------------------->

"""
path: /api/auth/login
method: POST
desc: endpoint to login into existing user account
"""
@auth_bp.route("/login", methods=["POST"])
@cross_origin()
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()

    if user and user.check_password(data["password"], user.password_hash):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({"access_token": access_token, "user_id": user.id}), 200

    return jsonify({"error": "Invalid credentials"}), 401

#<--------------------------- method end --------------------------------------->

"""
path: /api/auth/verify-token
method: GET
desc: endpoint to check token is expired or not
"""
@auth_bp.route("/verify-token", methods=["GET"])
@jwt_required()
def verify_token():
    return jsonify({"message": "not exprired"}), 200

#<--------------------------- method end --------------------------------------->