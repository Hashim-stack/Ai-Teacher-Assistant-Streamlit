def generate_mcqs(text):
    sentences = text.split(".")[:5]
    mcqs = []
    for s in sentences:
        if len(s.strip()) > 10:
            mcqs.append({
                "question": f"What is {s.strip()}?",
                "options": [
                    "Option A",
                    "Option B",
                    "Option C",
                    "Option D"
                ],
                "answer": "Option A"
            })
    return mcqs