"""
===========================================================
StudyMate AI - Supervisor Agent
===========================================================

Role:
------
The Supervisor Agent manages the complete
multi-agent workflow.

Responsibilities:
------------------
1. Decide which agent runs next.
2. Track completed agents.
3. Handle workflow failures.
4. Prepare final response.

"""

from agents.state import StudyMateState



def supervisor_agent(
        state: StudyMateState
) -> StudyMateState:


    print("=" * 60)
    print("SUPERVISOR AGENT RUNNING")
    print("=" * 60)


    completed = state.get(
        "completed_agents",
        []
    )


    # ----------------------------------------
    # Check Profile Agent
    # ----------------------------------------

    if "profile" not in completed:

        state["current_agent"] = "profile"

        print(
            "Next Agent : Profile Agent"
        )

        return state



    # ----------------------------------------
    # Check Planner Agent
    # ----------------------------------------

    if "planner" not in completed:

        state["current_agent"] = "planner"

        print(
            "Next Agent : Planner Agent"
        )

        return state



    # ----------------------------------------
    # Check Progress Agent
    # ----------------------------------------

    if "progress" not in completed:

        state["current_agent"] = "progress"

        print(
            "Next Agent : Progress Agent"
        )

        return state



    # ----------------------------------------
    # Check Recommendation Agent
    # ----------------------------------------

    if "recommendation" not in completed:

        state["current_agent"] = "recommendation"

        print(
            "Next Agent : Recommendation Agent"
        )

        return state



    # ----------------------------------------
    # Workflow Completed
    # ----------------------------------------

    state["current_agent"] = "end"



    state["final_response"] = (
        "StudyMate AI completed the complete "
        "student analysis workflow successfully."
    )


    print(
        "Workflow Completed Successfully"
    )


    return state