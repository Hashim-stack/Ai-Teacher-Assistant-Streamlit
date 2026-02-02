from difflib import SequenceMatcher

def evaluate_answer(model, student):
    similarity = SequenceMatcher(None, model.lower(), student.lower()).ratio()
    score = round(similarity * 10, 2)
    feedback = "Good understanding" if score > 6 else "Needs improvement"
    return score, feedback