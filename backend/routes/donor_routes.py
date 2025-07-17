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

    # Compute match scores for all donors
    matches = []
    for donor in donors:
         score = compute_match_score(patient, donor)
         matches.append({"donor": donor, "score": score})
    top_matches = sorted(matches, key=lambda x: x["score"], reverse=True)[:5]
    return jsonify({"recommendations": top_matches})
