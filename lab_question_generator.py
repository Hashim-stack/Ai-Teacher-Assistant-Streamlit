def generate_lab_questions(text):
    topics = text.split(".")[:5]
    return [f"Write a program related to {t.strip()}" for t in topics if t.strip()]