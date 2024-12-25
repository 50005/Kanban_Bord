from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from services.user_service import UserService
from database import get_db
from schemas.user import UserCreate, UserUpdate, UserAddToProject, UserRemoveFromProject, User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route("/", methods=["POST"])
def create_user():
    user = UserCreate(**request.get_json())
    db: Session = get_db()
    user_service = UserService(db)
    created_user = user_service.create_user(
        username=user.username,
        email=user.email,
        password=user.password
    )
    return jsonify(User.from_orm(created_user).dict()), 201


@user_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id: int):
    db: Session = get_db()
    user_service = UserService(db)
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(User.from_orm(user).dict()), 200

@user_blueprint.route("/username/<string:username>", methods=["GET"])
def get_user_by_username(username: str):
    db: Session = get_db()
    user_service = UserService(db)
    user = user_service.get_user_by_username(username)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(User.from_orm(user).dict()), 200


@user_blueprint.route("/", methods=["GET"])
def get_all_users():
    db: Session = get_db()
    user_service = UserService(db)
    users = user_service.get_all_users()
    return jsonify([User.from_orm(user).dict() for user in users]), 200


@user_blueprint.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id: int):
    user = UserUpdate(**request.get_json())
    db: Session = get_db()
    user_service = UserService(db)
    updated_user = user_service.update_user(
        user_id=user_id,
        username=user.username,
        email=user.email,
    )
    if not updated_user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(User.from_orm(updated_user).dict()), 200

@user_blueprint.route("/add_to_project", methods=["PUT"])
def add_user_to_project():
    user_project = UserAddToProject(**request.get_json())
    db: Session = get_db()
    user_service = UserService(db)
    user = user_service.add_user_to_project(
        user_id=user_project.user_id,
        project_id=user_project.project_id
    )
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(User.from_orm(user).dict()), 200

@user_blueprint.route("/remove_from_project", methods=["PUT"])
def remove_user_from_project():
    user_project = UserRemoveFromProject(**request.get_json())
    db: Session = get_db()
    user_service = UserService(db)
    user = user_service.remove_user_from_project(
        user_id=user_project.user_id,
        project_id=user_project.project_id
    )
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(User.from_orm(user).dict()), 200


@user_blueprint.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    db: Session = get_db()
    user_service = UserService(db)
    if not user_service.delete_user(user_id):
        return jsonify({"message": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200