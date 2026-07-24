"""
===========================================================
StudyMate AI - Profile Agent
===========================================================

Responsibilities
----------------
1. Validate student information.
2. Load the profile prompt.
3. Send prompt to Ollama.
4. Parse JSON response.
5. Store profile analysis.
6. Maintain execution logs.

"""

import json
import time

from agents.state import StudyMateState

from llm.ollama_client import OllamaClient

from utils.prompt_loader import load_prompt
from utils.validators import (
    validate_student_data,
    validate_json
)

client = OllamaClient()


def build_prompt(student: dict) -> str:
    """
    Builds the prompt from student information.
    """

    template = load_prompt("profile.txt")

    prompt = template.format(
        student_name=student.get("name", ""),
        department=student.get("department", ""),
        semester=student.get("semester", ""),
        cgpa=student.get("cgpa", ""),
        study_hours=student.get("study_hours_per_day", ""),
        goal=student.get("goal", ""),
        learning_style=student.get("learning_style", ""),
        attendance=student.get("attendance", ""),
        subjects=", ".join(student.get("subjects", [])),
        marks=json.dumps(
            student.get("marks", {}),
            indent=4
        ),
        exam_date=student.get("exam_date", "")
    )

    return prompt


def parse_response(response: str):
    """
    Convert LLM response to JSON.
    """

    try:

        data = json.loads(response)

        validate_json(data)

        return data

    except Exception:

        return None


def default_profile(error_message: str):
    """
    Returns fallback profile.
    """

    return {
        "student_summary": "Analysis Failed",

        "strengths": [],

        "weak_subjects": [],

        "learning_style_detected": "",

        "academic_risk": "Unknown",

        "priority_subjects": [],

        "best_study_method": "",

        "confidence_score": 0,

        "analysis": error_message
    }


def profile_agent(
    state: StudyMateState
) -> StudyMateState:
    """
    Main Profile Agent.
    """

    start_time = time.time()

    print("=" * 60)
    print("PROFILE AGENT STARTED")
    print("=" * 60)

    try:

        student = state["student"]

        validate_student_data(student)

    except Exception as e:

        state["profile_analysis"] = default_profile(str(e))

        return state

    prompt = build_prompt(student)

    system_prompt = """
You are StudyMate AI's Profile Analysis Agent.

Analyze the student's academic profile.

Always return ONLY VALID JSON.

Never include markdown.

Never explain anything.

Return ONLY JSON.
"""

    response = None

    max_retry = 3

    retry = 0

    while retry < max_retry:

        try:

            response = client.generate(
                system_prompt,
                prompt
            )

            parsed = parse_response(response)

            if parsed is not None:

                break

        except Exception:

            parsed = None

        retry += 1
            # -------------------------------------------------------
    # If JSON parsing failed after all retries
    # -------------------------------------------------------

    if parsed is None:

        state["profile_analysis"] = default_profile(
            "Unable to generate valid AI response."
        )

        state["chat_history"].append(
            {
                "role": "Profile Agent",
                "message": "Profile analysis failed."
            }
        )

        state["completed_agents"].append("profile")

        state["current_agent"] = "planner"

        print("Profile Agent Failed")

        return state

    # -------------------------------------------------------
    # Save Profile Analysis
    # -------------------------------------------------------

    state["profile_analysis"] = parsed

    # -------------------------------------------------------
    # Update Chat History
    # -------------------------------------------------------

    state["chat_history"].append(
        {
            "role": "Profile Agent",
            "message": "Student profile analyzed successfully."
        }
    )

    # -------------------------------------------------------
    # Update Workflow
    # -------------------------------------------------------

    if "profile" not in state["completed_agents"]:
        state["completed_agents"].append("profile")

    state["current_agent"] = "planner"

    # -------------------------------------------------------
    # Execution Time
    # -------------------------------------------------------

    execution_time = round(
        time.time() - start_time,
        2
    )

    print("=" * 60)
    print("PROFILE ANALYSIS COMPLETED")
    print("=" * 60)

    print(f"Student : {student.get('name')}")
    print(f"Execution Time : {execution_time} sec")

    print("\nLearning Style :")
    print(
        state["profile_analysis"].get(
            "learning_style_detected",
            "Unknown"
        )
    )

    print("\nAcademic Risk :")
    print(
        state["profile_analysis"].get(
            "academic_risk",
            "Unknown"
        )
    )

    print("\nWeak Subjects :")
    print(
        state["profile_analysis"].get(
            "weak_subjects",
            []
        )
    )

    print("\nPriority Subjects :")
    print(
        state["profile_analysis"].get(
            "priority_subjects",
            []
        )
    )

    print("\nConfidence Score :")
    print(
        state["profile_analysis"].get(
            "confidence_score",
            0
        )
    )

    print("=" * 60)

    return state