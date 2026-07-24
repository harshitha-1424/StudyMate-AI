"""
===========================================================
StudyMate AI - Recommendation Agent
===========================================================

Responsibilities
----------------
1. Analyze student performance.
2. Generate personalized guidance.
3. Suggest improvements.
4. Provide motivation.
5. Create adaptive next steps.

"""

import json
import time

from agents.state import StudyMateState

from llm.ollama_client import OllamaClient

from utils.prompt_loader import load_prompt
from utils.validators import validate_json


client = OllamaClient()



def build_recommendation_prompt(
        state: StudyMateState
) -> str:
    """
    Build recommendation prompt.
    """


    template = load_prompt(
        "recommendation.txt"
    )


    student = state.get(
        "student",
        {}
    )


    prompt = template.format(

        student_name=student.get(
            "name",
            ""
        ),

        department=student.get(
            "department",
            ""
        ),

        semester=student.get(
            "semester",
            ""
        ),

        goal=student.get(
            "goal",
            ""
        ),


        profile_analysis=json.dumps(
            state.get(
                "profile_analysis",
                {}
            ),
            indent=4
        ),


        study_plan=json.dumps(
            state.get(
                "study_plan",
                {}
            ),
            indent=4
        ),


        progress_report=json.dumps(
            state.get(
                "progress_report",
                {}
            ),
            indent=4
        )

    )


    return prompt




def parse_recommendations(
        response: str
):

    """
    Convert LLM output into JSON.
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



def default_recommendation(
        error
):

    return {

        "recommendations": [],

        "subject_improvement": [],

        "learning_techniques": [],

        "revision_strategy": [],

        "resource_suggestions": [],

        "daily_habits": [],

        "motivation_message":
            "Keep improving every day!",

        "next_steps": [],

        "error":
            str(error)

    }



def recommendation_agent(
        state: StudyMateState
) -> StudyMateState:


    start_time = time.time()


    print("=" * 60)
    print("RECOMMENDATION AGENT STARTED")
    print("=" * 60)



    prompt = build_recommendation_prompt(
        state
    )



    system_prompt = """

You are StudyMate AI Recommendation Agent.

You are a personal AI academic mentor.

Generate actionable recommendations.

Return ONLY JSON.

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


            parsed = parse_recommendations(
                response
            )


            if parsed:

                break


        except Exception:

            parsed = None


        retries += 1



    if parsed is None:

        state["recommendations"] = (
            default_recommendation(
                "Recommendation generation failed."
            )
        )

        state["chat_history"].append(
            {
                "role":
                    "Recommendation Agent",

                "message":
                    "Recommendation generation failed."
            }
        )

        return state
            # -------------------------------------------------------
    # Save Recommendations
    # -------------------------------------------------------

    state["recommendations"] = parsed.get(
        "recommendations",
        []
    )


    # -------------------------------------------------------
    # Save Motivation Message
    # -------------------------------------------------------

    state["motivation_message"] = parsed.get(
        "motivation_message",
        "Keep learning and improving!"
    )


    # -------------------------------------------------------
    # Update Conversation Memory
    # -------------------------------------------------------

    state["chat_history"].append(
        {
            "role":
                "Recommendation Agent",

            "message":
                "Personalized recommendations generated successfully."
        }
    )


    # -------------------------------------------------------
    # Update Workflow
    # -------------------------------------------------------

    if "recommendation" not in state["completed_agents"]:

        state["completed_agents"].append(
            "recommendation"
        )


    state["current_agent"] = "end"



    # -------------------------------------------------------
    # Create Final Response
    # -------------------------------------------------------

    state["final_response"] = {

        "profile":
            state.get(
                "profile_analysis",
                {}
            ),

        "study_plan":
            state.get(
                "study_plan",
                {}
            ),

        "progress":
            state.get(
                "progress_report",
                {}
            ),

        "recommendations":
            state.get(
                "recommendations",
                []
            ),

        "motivation":
            state.get(
                "motivation_message",
                ""
            )

    }



    # -------------------------------------------------------
    # Execution Information
    # -------------------------------------------------------

    execution_time = round(
        time.time() - start_time,
        2
    )


    print("=" * 60)
    print("RECOMMENDATION AGENT COMPLETED")
    print("=" * 60)


    print(
        "Recommendations Generated:"
    )

    print(
        len(
            state["recommendations"]
        )
    )


    print(
        "\nMotivation:"
    )

    print(
        state["motivation_message"]
    )


    print(
        "\nExecution Time:",
        execution_time,
        "seconds"
    )


    print("=" * 60)



    return state