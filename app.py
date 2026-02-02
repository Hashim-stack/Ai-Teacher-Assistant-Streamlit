import streamlit as st
from text_extractor import extract_text
from mcq_generator import generate_mcqs
from lab_question_generator import generate_lab_questions
from answer_evaluator import evaluate_answer

st.set_page_config(page_title="AI Teacher Assistant", layout="wide")

st.title("🎓 AI Teacher Assistant for Colleges")

if "notes_text" not in st.session_state:
    st.session_state.notes_text = ""
if "mcqs" not in st.session_state:
    st.session_state.mcqs = []
if "lab_questions" not in st.session_state:
    st.session_state.lab_questions = []

menu = st.sidebar.radio(
    "Select Module",
    ["Upload Notes", "MCQ Generator", "Lab Questions", "Answer Evaluation"]
)

if menu == "Upload Notes":
    uploaded = st.file_uploader("Upload Notes (TXT)", type=["txt"])
    if uploaded:
        st.session_state.notes_text = extract_text(uploaded)
        st.success("Notes uploaded successfully!")

elif menu == "MCQ Generator":
    if st.button("Generate MCQs"):
        st.session_state.mcqs = generate_mcqs(st.session_state.notes_text)

    for i, q in enumerate(st.session_state.mcqs, 1):
        st.write(f"**Q{i}. {q['question']}**")
        for opt in q["options"]:
            st.write(opt)
        st.write(f"✅ Answer: {q['answer']}")
        st.markdown("---")

elif menu == "Lab Questions":
    if st.button("Generate Lab Questions"):
        st.session_state.lab_questions = generate_lab_questions(st.session_state.notes_text)

    for i, q in enumerate(st.session_state.lab_questions, 1):
        st.write(f"{i}. {q}")

elif menu == "Answer Evaluation":
    model_ans = st.text_area("Model Answer")
    student_ans = st.text_area("Student Answer")
    if st.button("Evaluate"):
        score, feedback = evaluate_answer(model_ans, student_ans)
        st.success(f"Score: {score}/10")
        st.info(feedback)