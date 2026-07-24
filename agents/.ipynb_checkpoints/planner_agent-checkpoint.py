"""
===========================================================
StudyMate AI - Planner Agent
===========================================================

Responsibilities
----------------
1. Analyze student profile.
2. Understand weak subjects and priorities.
3. Generate personalized study plan using Ollama.
4. Create daily, weekly and revision schedules.
5. Update LangGraph state.

"""

import json
import time

from agents.state import StudyMateState

from llm.ollama_client import OllamaClient

from utils.prompt_loader import load_prompt
from utils.validators import validate_json


client = OllamaClient()


def build_planner_prompt(state: StudyMateState) -> str:
    """
    Creates planner prompt using profile information.
    """

    template = load_prompt("planner.txt")

    student = state.get("student", {})

    profile = state.get(
        "profile_analysis",
        {}
    )

    prompt = template.format(

        student_name=student.get(
            "name",
            ""
        ),

        semester=student.get(
            "semester",
            ""
        ),

        department=student.get(
            "department",
            ""
        ),

        study_hours=student.get(
            "study_hours_per_day",
            ""
        ),

        exam_date=student.get(
            "exam_date",
            ""
        ),

        subjects=", ".join(
            student.get(
                "subjects",
                []
            )
        ),

        profile_analysis=json.dumps(
            profile,
            indent=4
        )
    )

    return prompt


def parse_plan(response: str):
    """
    Parse LLM response into JSON.
    """

    try:

        data = json.loads(response)

        validate_json(data)

        return data

    except Exception:

        return None


def default_plan(error):
    """
    Fallback response.
    """

    return {

        "daily_schedule": [],

        "weekly_plan": {},

        "revision_plan": [],

        "pomodoro_sessions": [],

        "priority_subjects": [],

        "study_strategy":
            "Unable to generate plan.",

        "error": str(error)

    }


def planner_agent(
        state: StudyMateState
) -> StudyMateState:

    """
    Main Planner Agent.
    """

    start_time = time.time()


    print("=" * 60)
    print("PLANNER AGENT STARTED")
    print("=" * 60)


    prompt = build_planner_prompt(state)


    system_prompt = """

You are StudyMate AI Planner Agent.

Your task is to create a personalized
academic study plan.

Consider:

- Student available study hours
- Weak subjects
- Exam date
- Learning style
- Academic priorities


Return ONLY valid JSON.

Do not use markdown.

Do not add explanations.

"""


    parsed = None

    retry_count = 0

    max_retry = 3


    while retry_count < max_retry:

        try:

            response = client.generate(
                system_prompt,
                prompt
            )


            parsed = parse_plan(
                response
            )


            if parsed:

                break


        except Exception:

            parsed = None


        retry_count += 1
            # -------------------------------------------------------
    # If planning failed after retries
    # -------------------------------------------------------

    if parsed is None:

        state["study_plan"] = default_plan(
            "Planner Agent could not generate valid JSON."
        )

        state["chat_history"].append(
            {
                "role": "Planner Agent",
                "message": "Study plan generation failed."
            }
        )

        if "planner" not in state["completed_agents"]:
            state["completed_agents"].append(
                "planner"
            )

        state["current_agent"] = "progress"

        print("Planner Agent Failed")

        return state


    # -------------------------------------------------------
    # Save generated study plan
    # -------------------------------------------------------

    state["study_plan"] = parsed


    # -------------------------------------------------------
    # Update Conversation Memory
    # -------------------------------------------------------

    state["chat_history"].append(
        {
            "role": "Planner Agent",
            "message":
                "Personalized study plan generated successfully."
        }
    )


    # -------------------------------------------------------
    # Update Workflow Status
    # -------------------------------------------------------

    if "planner" not in state["completed_agents"]:

        state["completed_agents"].append(
            "planner"
        )


    state["current_agent"] = "progress"



    # -------------------------------------------------------
    # Execution Information
    # -------------------------------------------------------

    execution_time = round(
        time.time() - start_time,
        2
    )


    print("=" * 60)
    print("PLANNER AGENT COMPLETED")
    print("=" * 60)


    print(
        "Priority Subjects:"
    )

    print(
        state["study_plan"].get(
            "priority_subjects",
            []
        )
    )


    print(
        "\nExecution Time:",
        execution_time,
        "seconds"
    )


    print("=" * 60)


    return state