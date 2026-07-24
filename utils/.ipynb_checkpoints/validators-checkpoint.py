"""
validators.py

Validation functions for StudyMate AI.
"""


def validate_student_data(student: dict) -> bool:
    """
    Validate required student fields.
    """

    required_fields = [
        "name",
        "department",
        "semester",
        "cgpa",
        "study_hours_per_day",
        "goal",
        "subjects",
        "exam_date"
    ]

    for field in required_fields:
        if field not in student:
            raise ValueError(f"Missing required field: {field}")

        if student[field] in ("", None):
            raise ValueError(f"{field} cannot be empty")

    return True


def validate_json(data: dict) -> bool:
    """
    Check whether parsed JSON is valid.
    """

    if not isinstance(data, dict):
        raise ValueError("LLM output is not a dictionary.")

    return True