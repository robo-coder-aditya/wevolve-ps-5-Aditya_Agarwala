# app/main.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.data import skills, roles, levelTransitions

app = FastAPI()

# static files (for images, css, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "input.html",
        {"request": request}
    )


@app.post("/applications", response_class=HTMLResponse)
async def applications(
    request: Request,
    currentRole: str = Form(...),
    targetRole: str = Form(...),
    experience: float = Form(...),
    education: str = Form(...),
    skills_selected: list[str] = Form(None)
):
    # ---------- Input validation ----------
    if not skills_selected:
        return templates.TemplateResponse(
            "input.html",
            {
                "request": request,
                "errorMessage": "Please select at least one skill"
            }
        )

    currentExperience = experience
    currentSkills = skills_selected

    # ---------- Skill Matching ----------
    matched_skills = []
    missing_skills = []

    required_skills = roles[targetRole]["skillset"]

    for skill in required_skills:
        if skill in currentSkills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    matched_count = len(matched_skills)
    missing_count = len(missing_skills)

    skill_gap_percentage = (
        (len(required_skills) - matched_count) / len(required_skills)
    ) * 100

    # ---------- Experience Score ----------
    experience_score = 50
    required_experience = roles[targetRole]["experience_years"]

    if required_experience[0] <= currentExperience <= required_experience[1]:
        experience_score = 100
    elif currentExperience < required_experience[0]:
        diff = required_experience[0] - currentExperience
        ratio = diff / required_experience[0]
        experience_score = max(0, 100 - ratio * 100)
    else:
        experience_score = 90

    readiness_score = (100 - skill_gap_percentage) * 0.8 + experience_score * 0.2

    # ---------- Learning Roadmap ----------
    learning_dashboard = []
    estimatedTime = 0

    phase1Count = 0
    phase2Count = 0

    for skill in missing_skills:
        phase = 1
        if skills[skill]["prerequisites"]:
            phase = 2

        duration = skills[skill]["learning_time_months"]
        estimatedTime += duration

        focus = skills[skill]["primary_focus"]

        if phase == 1:
            if phase1Count < 3:
                priority = "High"
            elif phase1Count < 6:
                priority = "Medium"
            else:
                priority = "Low"
            phase1Count += 1
        else:
            if phase2Count < 3:
                priority = "High"
            elif phase2Count < 6:
                priority = "Medium"
            else:
                priority = "Low"
            phase2Count += 1

        learning_dashboard.append({
            "phase": phase,
            "duration": duration,
            "focus": focus,
            "skill": skill,
            "priority": priority,
            "prerequisites": skills[skill]["prerequisites"],
            "reasoning": skills[skill]["reason_to_learn"],
            "recommended_resources": ", ".join(skills[skill]["recommended_resources"])
        })


    # ---------- Level Transition ----------
    differenceLevel = roles[targetRole]["level"] - roles[currentRole]["level"]

    successRate = 100
    average_time = 0

    if differenceLevel > 0:
        transitionData = next(
            (t for t in levelTransitions if t["level_difference"] == differenceLevel),
            None
        )
        if transitionData:
            successRate = transitionData["success_rate_percent"]
            average_time = transitionData["avg_transition_time_months"]

    # ---------- Render Output ----------
    return templates.TemplateResponse(
        "output.html",
        {
            "request": request,
            "currentRole": currentRole,
            "currentEducation": education,
            "currentExperience": currentExperience,
            "targetRole": targetRole,
            "requiredExperience": required_experience,
            "numberOfSkills": len(required_skills),
            "skill_gap_percentage": skill_gap_percentage,
            "readiness_score": readiness_score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "matched_count": matched_count,
            "missing_count": missing_count,
            "estimatedTime": estimatedTime,
            "successRate": successRate,
            "average_time": average_time,
            "learning_dashboard": learning_dashboard
        }
    )
