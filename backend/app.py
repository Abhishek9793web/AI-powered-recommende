# Main Flask application

from flask import Flask, request, jsonify
from flask_cors import CORS

from nlp.extract_info import parse_transfusion_report
from services.matcher import compute_match_score


from routes.patient_routes import patient_routes
from routes.donor_routes import donor_routes

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend




app.register_blueprint(patient_routes)
app.register_blueprint(donor_routes)

# === Route: Home ===
@app.route('/')
def home():
    return jsonify({"message": "Smart Blood Matching API is running."})

# === Route: NLP Report Parser ===
@app.route('/parse-report', methods=['POST'])
def parse_report():
    data = request.get_json()
    text = data.get('report_text', '')
    if not text:
        return jsonify({"error": "No report_text provided"}), 400

    parsed_data = parse_transfusion_report(text)
    return jsonify(parsed_data)

# === Route: Recommend Blood Units ===
@app.route('/recommend-units', methods=['POST'])
def recommend_units():
    data = request.get_json()
    patient = data.get("patient", {})
    donors = data.get("donors", [])

    if not patient or not donors:
        return jsonify({"error": "Patient or donor data missing"}), 400

    matches = []
    for donor in donors:
        score = compute_match_score(patient, donor)
        matches.append({"donor": donor, "score": score})

    # Sort by score descending and take top 5
    top_matches = sorted(matches, key=lambda x: x["score"], reverse=True)[:5]
    return jsonify({"recommendations": top_matches})

# === Main Runner ===
if __name__ == '__main__':
    app.run(debug=True)

