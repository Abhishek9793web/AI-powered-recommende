def compute_match_score(patient, unit):
    score = 0

    # Exact blood type match (+1)

    if patient['blood_type'] == unit['blood_type']:
        score += 1

    if isinstance(patient, list):
        patient = patient[0]  # TEMP workaround, optional    

    # Check for antibody conflicts (hard penalty if conflict)
    unit_antigens = set(unit.get('minor_antigens', []))
    patient_antibodies = set(patient.get('known_antibodies', []))
    conflict = any(ab.replace("Anti-", "") in unit_antigens for ab in patient_antibodies)

    if conflict:
        return 0  # incompatible, high-risk

    score += 2  # if no conflict, award bonus

    # Freshness of unit (+1)
    if unit.get('is_fresh'):
        score += 1

    # Rare match bonus (if patient has rare blood type)
    if patient['blood_type'] in ['AB-', 'O-']:
        score += 1

    return score
    
 

