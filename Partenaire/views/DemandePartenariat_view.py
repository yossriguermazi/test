from typing import Any
from config.db_utils import jsonResponse
from flask import Blueprint, request
from controllers.DeamandePartenariat_controller import DemandePartenariatController
from models.criteria import Criteria
from flask import jsonify
from werkzeug.exceptions import NotFound, BadRequest

DeamndePartenaire_bp = Blueprint("DeamndePartenaire_blueprint", __name__)
controller = DemandePartenariatController()

@DeamndePartenaire_bp.route('/DeamndePartenaires' , methods=["GET"])
def findAll() -> dict:
    try:
        limit = request.args.get("limit", 10, type=int)
        page = request.args.get("page", 1, type=int)
        name = request.args.get("name")
        type = request.args.get("type")
        countryName = request.args.get("countryName")
        criteria = Criteria(name=name, type=type, countryName=countryName)
        results = controller.findAll(criteria)
        return jsonResponse(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@DeamndePartenaire_bp.route('/DeamndePartenaires/<string:_id>', methods=["GET"])
def findOne(_id: str) -> dict[str, Any]:
    try:
        return jsonResponse(controller.findOne(_id))
    except NotFound:
        return jsonify({"error": f"No such document for the identifier = {_id}."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@DeamndePartenaire_bp.route('/DeamndePartenaires/<string:_id>', methods=["PUT", "PATCH"])
def update(_id: str) -> dict[str, Any]:
    body = request.get_json(force=True)
    try:
        return jsonResponse(controller.update(_id, body))
    except BadRequest:
        return jsonify({"error": "Invalid request data."}), 400
    except Exception as e:
        return jsonify({"error": f"Document update error: {e}."}), 500


@DeamndePartenaire_bp.route('/DeamndePartenaires', methods=["POST"])
def insert() -> dict[str, Any]:
    body = request.get_json(force=True)
    try:
        return jsonResponse(controller.insert(body))
    except BadRequest:
        return jsonify({"error": "Invalid request data."}), 400
    except Exception as e:
        return jsonify({"error": f"Document insertion error: {e}."}), 500


@DeamndePartenaire_bp.route('/DeamndePartenaires/<string:_id>', methods=["DELETE"])
def remove(_id: str) -> dict[str, Any]:
    try:
        return jsonResponse(controller.remove(_id))
    except NotFound:
        return jsonify({"error": f"No such document for the id = {_id}."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
