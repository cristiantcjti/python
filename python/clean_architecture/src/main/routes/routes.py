from flask import Blueprint, request, jsonify

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer
from src.validators.user_finder_validator import user_finder_validator
from src.validators.user_register_validator import user_register_validator

user_route_bp = Blueprint("user_route", __name__)

from src.errors.types.error_handler import handle_errors


@user_route_bp.route("/user/find", methods=["GET"])
def user_find():
    http_response = None
    try:
        user_finder_validator(request)
        http_response = request_adapter(request, user_finder_composer())
    except Exception as e:
        http_response = handle_errors(e)

    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/user", methods=["POST"])
def register_user():
    http_response = None
    try:
        user_register_validator(request)
        http_response = request_adapter(request, user_register_composer())
    except Exception as e:
        http_response = handle_errors(e)

    return jsonify(http_response.body), http_response.status_code
