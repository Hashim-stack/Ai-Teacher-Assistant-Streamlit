# 🎓 AI Teacher Assistant for Colleges  
> _Education automation powered by AI — not just another chatbot_

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)
![Open Source](https://img.shields.io/badge/Open--Source-Yes-orange)

---

## 🚀 Overview
**AI Teacher Assistant for Colleges** is a lightweight, AI-powered application designed to automate key academic tasks such as question paper creation and answer evaluation.

Instead of focusing on chat-based AI, this project targets **real academic workflows** — helping teachers save time while improving consistency and efficiency.
> ⚡ No database  
> 🧠 Session-based AI logic  
> 🎓 Built for real classroom use  

---

## ✨ What Makes This Project Special?

✔ Not a generic chatbot  
✔ Focuses on **education automation**  
✔ Uses **session state instead of a database**  
✔ Easy to run, demo, and explain  
✔ Recruiter-friendly project structure  

---

## 🧠 Core Features

### 📄 Upload Academic Notes
- Upload subject notes (`.txt`)
- Content is processed and stored in session memory

---

### ❓ Automatic MCQ Generator
- Generates MCQs from uploaded notes
- Includes:
  - Question
  - Multiple options
  - Correct answer
- Ideal for tests, quizzes, and exams

---

### 🧪 Lab Question Generator
- Automatically creates lab/programming questions
- Useful for:
  - Practical exams
  - Assignments
  - Lab sessions

---

### 📝 Answer Evaluation (Auto-Grading)
- Compare **Model Answer vs Student Answer**
- Uses text similarity (not exact matching)
- Supports **partial marking**
- Provides:
  - Score (out of 10)
  - Feedback message

---

## 🖥️ Application Screens (Flow)
Upload Notes
↓
Generate MCQs / Lab Questions
↓
Evaluate Student Answers
↓
Instant Score & Feedback


---

## 🛠️ Tech Stack
| Layer | Technology |
|-----|-----------|
| Language | Python |
| UI | Streamlit |
| AI Logic | Text Similarity (NLP) |
| State Management | Streamlit Session State |
| Storage | ❌ None (Session-based) |

---

## 📁 Project Structure
ai-teacher-assistant/
│
├── app.py # Main Streamlit application
├── text_extractor.py # Reads uploaded notes
├── mcq_generator.py # MCQ generation logic
├── lab_question_generator.py # Lab question generator
├── answer_evaluator.py # Auto-grading logic
├── requirements.txt
└── README.md


---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Hashim-stack/Ai-Teacher-Assistant-Streamlit.git
cd Ai-Teacher-Assistant

2️⃣ (Optional) Create Virtual Environment
python -m venv venv


Activate:
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py


Open browser at:
http://localhost:8501

🧪 Sample Test (Answer Evaluation)

Model Answer
Python is a programming language used for data analysis and software development.
Student Answer
Python is a programming language mainly used for data analysis.


✔ Output:
Score: 7–9 / 10

Feedback: Good understanding

🎤 How to Explain This in Interviews / Viva
“This project automates academic tasks like question generation and answer evaluation using AI techniques. To keep it lightweight and demo-friendly, Streamlit session state is used instead of a database.”

🚀 Future Enhancements
🔌 Open-source LLM integration (Ollama / Mistral)
📄 PDF upload support
🎯 Difficulty-level based MCQs
📊 Teacher analytics dashboard
📈Database integration
📤 Export questions to PDF



👨‍💻 Ideal For
Final Year Projects
AI / Python Portfolios
Hackathons
College Demos
Resume Projects


📜 License
This project is open-source and free to use for educational purposes.


Thankyou❤️
