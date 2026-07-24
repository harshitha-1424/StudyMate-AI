"""
StudyMate AI - Report Generator
Creates final student performance report
"""

from datetime import datetime


def generate_report(result):

    student = result.get("student", {})
    profile = result.get("profile_analysis", {})
    plan = result.get("study_plan", {})
    progress = result.get("progress_report", {})
    recommendations = result.get("recommendations", [])


    report = f"""
============================================================
                STUDYMATE AI REPORT
============================================================

Generated On:
{datetime.now().strftime("%d-%m-%Y")}


------------------------------------------------------------
STUDENT PROFILE
------------------------------------------------------------

Name:
{student.get("name")}

Department:
{student.get("department")}

Semester:
{student.get("semester")}

CGPA:
{student.get("cgpa")}

Attendance:
{student.get("attendance")}%



------------------------------------------------------------
PROFILE ANALYSIS
------------------------------------------------------------

Summary:
{profile.get("student_summary","")}


Strengths:
{profile.get("strengths",[])}


Weak Subjects:
{profile.get("weak_subjects",[])}


Academic Risk:
{profile.get("academic_risk","")}


Learning Style:
{profile.get("learning_style_detected","")}



------------------------------------------------------------
PERSONALIZED STUDY PLAN
------------------------------------------------------------

Daily Schedule:

"""

    for item in plan.get("daily_schedule",[]):

        report += f"""
Time:
{item.get("time")}

Subject:
{item.get("subject")}

Activity:
{item.get("activity")}

Duration:
{item.get("duration")}

----------------------------
"""


    report += f"""

------------------------------------------------------------
PROGRESS REPORT
------------------------------------------------------------

Performance Level:
{progress.get("performance_level","")}

Exam Readiness Score:
{progress.get("exam_readiness_score","")}/100


Weak Areas:

{progress.get("weak_areas",[])}



------------------------------------------------------------
AI RECOMMENDATIONS
------------------------------------------------------------

"""

    for r in recommendations:
        report += f"- {r}\n"


    report += f"""

------------------------------------------------------------
MOTIVATION
------------------------------------------------------------

{result.get("motivation_message","")}


============================================================
              END OF REPORT
============================================================
"""


    return report