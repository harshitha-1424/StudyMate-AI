"""
===========================================================
StudyMate AI - LangGraph Workflow
===========================================================

Connects:

Supervisor Agent
        |
        |
Profile Agent
        |
Planner Agent
        |
Progress Agent
        |
Recommendation Agent
        |
        END

"""

from langgraph.graph import StateGraph, END


from agents.state import StudyMateState

from agents.supervisor_agent import supervisor_agent

from agents.profile_agent import profile_agent

from agents.planner_agent import planner_agent

from agents.progress_agent import progress_agent

from agents.recommendation_agent import recommendation_agent



# ==========================================================
# Create Graph
# ==========================================================

workflow = StateGraph(
    StudyMateState
)



# ==========================================================
# Add Agents as Nodes
# ==========================================================

workflow.add_node(
    "supervisor",
    supervisor_agent
)


workflow.add_node(
    "profile",
    profile_agent
)


workflow.add_node(
    "planner",
    planner_agent
)


workflow.add_node(
    "progress",
    progress_agent
)


workflow.add_node(
    "recommendation",
    recommendation_agent
)



# ==========================================================
# Starting Point
# ==========================================================

workflow.set_entry_point(
    "supervisor"
)



# ==========================================================
# Supervisor Routing Logic
# ==========================================================

def route_agent(
        state: StudyMateState
):

    return state[
        "current_agent"
    ]



workflow.add_conditional_edges(

    "supervisor",

    route_agent,

    {

        "profile":
            "profile",

        "planner":
            "planner",

        "progress":
            "progress",

        "recommendation":
            "recommendation",

        "end":
            END
    }

)



# ==========================================================
# Return to Supervisor after every agent
# ==========================================================

workflow.add_edge(
    "profile",
    "supervisor"
)


workflow.add_edge(
    "planner",
    "supervisor"
)


workflow.add_edge(
    "progress",
    "supervisor"
)


workflow.add_edge(
    "recommendation",
    "supervisor"
)



# ==========================================================
# Compile Graph
# ==========================================================

graph = workflow.compile()