def check_risk_level(score):
    if score == 0:
        return "High Risk"
    elif score <= 2:
        return "Moderate Risk"
    else:
        return "Low Risk"
