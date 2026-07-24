from typing import TypedDict, Dict, List, Any


class StudyMateState(TypedDict):
    """
    Shared state used by every LangGraph agent.
    """

    # ======================================================
    # Student Input
    # ======================================================

    student: Dict[str, Any]
    """
    {
        "name": "",
        "semester": "",
        "department": "",
        "cgpa": 0.0,
        "study_hours_per_day": 0,
        "learning_style": "",
        "goal": "",
        "exam_date": "",
        "subjects": [],
        "marks": {},
        "attendance": 0
    }
    """

    # ======================================================
    # Profile Agent
    # ======================================================

    profile_analysis: Dict[str, Any]

    # ======================================================
    # Planner Agent
    # ======================================================

    study_plan: Dict[str, Any]

    # ======================================================
    # Progress Agent
    # ======================================================

    progress_report: Dict[str, Any]

    # ======================================================
    # Recommendation Agent
    # ======================================================

    recommendations: List[str]

    motivation_message: str

    # ======================================================
    # Supervisor
    # ======================================================

    current_agent: str

    completed_agents: List[str]

    # ======================================================
    # Conversation Memory
    # ======================================================

    chat_history: List[Dict[str, str]]

    # ======================================================
    # Final Output
    # ======================================================

    final_response: str