from flask import Blueprint, request, jsonify
from nlp.extract_info import parse_transfusion_report

report_parser = Blueprint('report_parser', __name__)

@report_parser.route('/parse-report', methods=['POST'])
def parse_report():
    data = request.json
    text = data.get('report_text', '')
    if not text:
        return jsonify({"error": "No report text provided"}), 400

    result = parse_transfusion_report(text)
    return jsonify(result)
