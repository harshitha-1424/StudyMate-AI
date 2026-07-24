"""
===========================================================
StudyMate AI - Progress Agent
===========================================================

Responsibilities
----------------
1. Analyze student learning progress.
2. Evaluate completed and pending tasks.
3. Measure exam readiness.
4. Identify weak areas.
5. Generate improvement strategies.

"""

import json
import time

from agents.state import StudyMateState

from llm.ollama_client import OllamaClient

from utils.prompt_loader import load_prompt
from utils.validators import validate_json


client = OllamaClient()



def build_progress_prompt(
        state: StudyMateState
) -> str:
    """
    Creates progress analysis prompt.
    """

    template = load_prompt(
        "progress.txt"
    )

    student = state.get(
        "student",
        {}
    )

    study_plan = state.get(
        "study_plan",
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

        exam_date=student.get(
            "exam_date",
            ""
        ),


        study_plan=json.dumps(
            study_plan,
            indent=4
        ),


        completed_tasks=json.dumps(
            state.get(
                "completed_tasks",
                []
            ),
            indent=4
        ),


        pending_tasks=json.dumps(
            state.get(
                "pending_tasks",
                []
            ),
            indent=4
        ),


        quiz_scores=json.dumps(
            state.get(
                "quiz_scores",
                {}
            ),
            indent=4
        ),


        study_hours=student.get(
            "study_hours_per_day",
            0
        ),


        attendance=student.get(
            "attendance",
            0
        )

    )


    return prompt



def parse_progress(
        response: str
):
    """
    Converts LLM output into JSON.
    """

    try:

        data = json.loads(
            response
        )

        validate_json(
            data
        )

        return data


    except Exception:

        return None



def default_progress(
        error
):

    return {

        "completion_percentage": 0,

        "study_consistency_score": 0,

        "exam_readiness_score": 0,

        "performance_level":
            "Unknown",

        "completed_strengths": [],

        "weak_areas": [],

        "subjects_to_improve": [],

        "improvement_actions": [],

        "risk_prediction":
            "Unknown",

        "progress_summary":
            "Analysis failed",

        "motivation_message":
            str(error)

    }



def progress_agent(
        state: StudyMateState
) -> StudyMateState:


    start_time = time.time()


    print("=" * 60)
    print("PROGRESS AGENT STARTED")
    print("=" * 60)



    prompt = build_progress_prompt(
        state
    )



    system_prompt = """

You are StudyMate AI Progress Agent.

Analyze student performance data.

Identify progress,
weaknesses,
risk areas,
and improvements.

Return ONLY valid JSON.

No markdown.

No explanations.

"""



    parsed = None


    retries = 0


    while retries < 3:


        try:

            response = client.generate(
                system_prompt,
                prompt
            )


            parsed = parse_progress(
                response
            )


            if parsed:

                break


        except Exception:

            parsed = None


        retries += 1



    if parsed is None:


        state["progress_report"] = default_progress(
            "Unable to generate progress analysis."
        )


        state["chat_history"].append(
            {
                "role":
                    "Progress Agent",

                "message":
                    "Progress analysis failed."
            }
        )


        if "progress" not in state["completed_agents"]:

            state["completed_agents"].append(
                "progress"
            )


        state["current_agent"] = "recommendation"


        return state
            # -------------------------------------------------------
    # Save Progress Analysis
    # -------------------------------------------------------

    state["progress_report"] = parsed


    # -------------------------------------------------------
    # Save Motivation Message
    # -------------------------------------------------------

    state["motivation_message"] = parsed.get(
        "motivation_message",
        "Keep working consistently!"
    )


    # -------------------------------------------------------
    # Update Conversation Memory
    # -------------------------------------------------------

    state["chat_history"].append(
        {
            "role": "Progress Agent",

            "message":
                "Student progress analyzed successfully."
        }
    )


    # -------------------------------------------------------
    # Update Workflow Status
    # -------------------------------------------------------

    if "progress" not in state["completed_agents"]:

        state["completed_agents"].append(
            "progress"
        )


    state["current_agent"] = "recommendation"



    # -------------------------------------------------------
    # Execution Information
    # -------------------------------------------------------

    execution_time = round(
        time.time() - start_time,
        2
    )


    print("=" * 60)
    print("PROGRESS AGENT COMPLETED")
    print("=" * 60)


    print(
        "Performance Level:"
    )

    print(
        state["progress_report"].get(
            "performance_level",
            "Unknown"
        )
    )


    print(
        "\nCompletion Percentage:"
    )

    print(
        state["progress_report"].get(
            "completion_percentage",
            0
        ),
        "%"
    )


    print(
        "\nExam Readiness Score:"
    )

    print(
        state["progress_report"].get(
            "exam_readiness_score",
            0
        )
    )


    print(
        "\nWeak Areas:"
    )

    print(
        state["progress_report"].get(
            "weak_areas",
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