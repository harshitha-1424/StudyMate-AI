# 🎓 StudyMate AI

StudyMate AI is an AI-powered multi-agent academic assistant designed to analyze a student's academic profile, generate personalized study plans, monitor learning progress, and provide intelligent recommendations to improve exam readiness.

The project is built using **LangGraph**, **Ollama LLM**, and a **Supervisor-Agent architecture**, where multiple AI agents collaborate to perform different academic analysis tasks.

---

# 🚀 Features

- 👤 Student Profile Analysis
- 📚 Personalized Study Plan Generation
- 📈 Academic Progress Evaluation
- 💡 AI-Based Study Recommendations
- 🤖 Multi-Agent Workflow using LangGraph
- 🧠 Local LLM Integration with Ollama
- 🔄 Supervisor Agent for Intelligent Routing
- 📊 Structured JSON Outputs

---

# 🛠️ Tech Stack

- Python
- LangGraph
- Ollama
- Llama 3 (Local LLM)
- Jupyter Notebook
- JSON
- Git & GitHub

---

# 📂 Project Structure

```
StudyMate-AI/
│
├── agents/
│   ├── profile_agent.py
│   ├── planner_agent.py
│   ├── progress_agent.py
│   ├── recommendation_agent.py
│   ├── supervisor_agent.py
│   └── state.py
│
├── llm/
│   └── ollama_client.py
│
├── prompts/
│   ├── profile.txt
│   ├── planner.txt
│   ├── progress.txt
│   └── recommendation.txt
│
├── utils/
│   ├── prompt_loader.py
│   ├── validators.py
│   └── json_parser.py
│
├── workflow/
│   └── graph.py
│
├── notebook/
│   └── StudyMate_AI.ipynb
│
├── images/
│   ├── architecture.png
│   ├── profile_agent.png
│   ├── planner_agent.png
│   ├── progress_agent.png
│   └── recommendation_agent.png
│
├── requirements.txt
└── README.md
```

---

# 🏗️ System Architecture

![Architecture](images/architecture.png)

The system follows a Supervisor-Agent architecture where the Supervisor Agent controls the workflow and routes execution among specialized AI agents.

---

# 🤖 Multi-Agent Workflow

1. **Supervisor Agent**
   - Controls the complete workflow.
   - Decides which agent executes next.

2. **Profile Agent**
   - Analyzes student academic information.
   - Identifies strengths, weaknesses, learning style, and academic risk.

3. **Planner Agent**
   - Generates personalized study schedules.
   - Creates revision strategies and weekly plans.

4. **Progress Agent**
   - Evaluates study progress.
   - Calculates completion percentage and exam readiness.

5. **Recommendation Agent**
   - Provides personalized recommendations.
   - Generates motivational feedback.

---
# 📸 Sample Outputs

## Profile Agent

![Profile Agent](./images/profile_agent.png)

---

## Planner Agent

![Planner Agent](./images/planner_agent.png)

---

## Progress Agent

![Progress Agent](./images/progress_agent.png)

---

## Recommendation Agent

![Recommendation Agent](./images/recommendation_agent.png)

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/your-username/StudyMate-AI.git
```

Move into the project directory.

```bash
cd StudyMate-AI
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Start the Ollama server.

```bash
ollama serve
```

Download the required LLM.

```bash
ollama pull llama3
```

Launch Jupyter Notebook.

```bash
jupyter notebook
```

Open the notebook and execute all cells.

---

# ▶️ Usage

1. Enter the student's academic details.
2. Run the notebook.
3. The Supervisor Agent automatically coordinates all AI agents.
4. The system generates:
   - Student Profile Analysis
   - Personalized Study Plan
   - Progress Report
   - Intelligent Recommendations

---

# 📈 Sample Workflow

```
Student Input
      │
      ▼
Supervisor Agent
      │
      ▼
Profile Agent
      │
      ▼
Planner Agent
      │
      ▼
Progress Agent
      │
      ▼
Recommendation Agent
      │
      ▼
Final Student Analysis
```

---

# 🔮 Future Enhancements

- Interactive Dashboard using Streamlit
- Performance Visualization Charts
- Quiz Generation Agent
- Attendance Prediction
- Study Reminder Notifications
- Voice-Based Academic Assistant
- Multi-Student Analytics
- Cloud Deployment

---

# 👩‍💻 Author

**Harshitha Empalli**

B.Tech - Computer Science Engineering (AI & ML)

---

# ⭐ Acknowledgements

- AMD AI PC Workshop
- LangGraph
- Ollama
- Llama 3
- Python Open Source Community