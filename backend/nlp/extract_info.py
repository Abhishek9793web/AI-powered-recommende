import re
from datetime import datetime

# Define keywords
ANTIBODY_PATTERN = r"Anti-[A-Za-z]+"
REACTIONS = ["Febrile", "Hemolytic", "Urticarial", "Allergic", "Anaphylactic"]
BLOOD_TYPE_PATTERN = r"\b(?:A|B|AB|O)[+-]"
DATE_PATTERN = r"\b(?:\d{1,2}[-/ ](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/ ]\d{2,4}|\d{4}-\d{2}-\d{2})\b"

def extract_antibodies(text):
    return re.findall(ANTIBODY_PATTERN, text)

def extract_reactions(text):
    return [reaction for reaction in REACTIONS if reaction.lower() in text.lower()]

def extract_dates(text):
    return re.findall(DATE_PATTERN, text)

def extract_blood_type(text):
    match = re.search(BLOOD_TYPE_PATTERN, text)
    return match.group() if match else None


def parse_transfusion_report(text):
    return {
        "antibodies": extract_antibodies(text),
        "reactions": extract_reactions(text),
        "transfusion_dates": extract_dates(text),
        "blood_type": extract_blood_type(text)
    }

# Example usage
if __name__ == "__main__":
    sample_text = """
    Patient has blood group B+ and developed Anti-K and Anti-E after transfusion on 12 Feb 2024.
    Noted reactions were Febrile and Urticarial.
    """
    result = parse_transfusion_report(sample_text)
    print(result)
