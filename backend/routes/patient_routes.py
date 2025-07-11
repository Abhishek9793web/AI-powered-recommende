# routes/patient_routes.py

from flask import Blueprint, request, jsonify
from nlp.extract_info import parse_transfusion_report

patient_routes = Blueprint("patient_routes", __name__)

@patient_routes.route("/parse-report", methods=["POST"])
def parse_report():
    data = request.get_json()
    text = data.get("report_text", "")
    if not text:
        return jsonify({"error": "Missing report_text"}), 400
    result = parse_transfusion_report(text)
    return jsonify(result)
