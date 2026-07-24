from typing import TypedDict, List, Dict, Any


class StudyMateState(TypedDict):
    # Student Information
    student_name: str
    semester: str
    subjects: List[str]
    study_hours: int
    exam_date: str

    # Agent Outputs
    profile: Dict[str, Any]
    study_plan: Dict[str, Any]
    progress: Dict[str, Any]
    recommendations: List[str]

    # Workflow
    current_agent: str
    final_response: str