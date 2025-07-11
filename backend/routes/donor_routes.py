# routes/donor_routes.py

from flask import Blueprint, request, jsonify
from services.matcher import compute_match_score

donor_routes = Blueprint("donor_routes", __name__)

@donor_routes.route("/recommend-units", methods=["POST"])
def recommend_units():
    data = request.get_json()
    patient = data.get("patient", {})
    donors = data.get("donors", [])
    if not patient or not donors:
        return jsonify({"error": "Missing patient or donor data"}), 400

    recommendations = compute_match_score(patient, donors)
    return jsonify({"recommendations": recommendations})
