from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.user import User
from app.database import db

user_bp = Blueprint("user", __name__)

"""
path: /api/users/:user_id
method: GET
desc: endpoint to get the user details by user_id
"""
@user_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "user not found"}), 404

    try:
        return (
            jsonify(
                {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role,
                    "is_verified": user.is_verified,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "mobile_no": user.mobile_no,
                }
            ),
            200,
        )
    except Exception as e:
        print(e)
        return jsonify({"message": "server internal error", "status": 500}), 500

#<--------------------------- method end --------------------------------------->

"""
path: /api/users
method: GET
desc: endpoint to get the all user details
"""
@user_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_users():
    print("inside the  get all user")
    users = User.query.all()

    return (
        jsonify(
            [
                {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role,
                    "is_verified": user.is_verified,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "mobile_no": user.mobile_no,
                }
                for user in users
            ]
        ),
        200,
    )
#<--------------------------- method end --------------------------------------->