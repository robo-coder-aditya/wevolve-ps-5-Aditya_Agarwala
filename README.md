<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/56f53835-89e4-4116-953d-0bca987f9c9a" />## Nucli - Skill Gap Analysis Engine
- Helps job seekers how ready they are for a target role, and generates a learning roadmap.
- Deployed as a production ready FastAPI web service

## Live Demo
- Deployed Application
  https://nucli-os.onrender.com/
## Features
- Job seekers have to input their current role from the dropdown, then select the skills they currently have, then mention their experience and target role.
- A predefined JSON dataset containing
   1. 63 Skills: Each skill has an estimated learning time, a reason to learn, primary focus. The skill might or might not have a prerequisite.
   2. 15 Roles: Each role has a difficulty level, a required skillset, and preferred experience
- Matched skills vs Missing skills analysis
- Calculates skill-gap percentage using (missingSkills/TotalSkills)*100
- Calculates readiness score using skill gap percentage and experience matching.
- Calculates total estimated time to cover all skills.
- Returns Average success rate and transition time for similar transitions
- Learning Roadmap Generation
    Dependency-wise phase allocation - phase 1 for skills with no prerequisites, and phase 2 for skills with prerequisites
    Priority-based ordering
    Estimated Learning Time
    Clear reasoning for each skill
    Recommended resources to learn from
- Some screenshots of the application
<img width="1894" height="871" alt="image" src="https://github.com/user-attachments/assets/5dd61a30-bf8c-4684-a932-06e60b2706bf" />
<img width="1899" height="871" alt="image" src="https://github.com/user-attachments/assets/9db519ae-2b97-4ba8-a0cd-710873a21ae1" />
<img width="1900" height="875" alt="image" src="https://github.com/user-attachments/assets/82aa52c8-02be-44da-90ee-5303dc043d4c" />
<img width="1901" height="874" alt="image" src="https://github.com/user-attachments/assets/332fcdcc-91b9-49e8-ad24-d0772c6ec37d" />

## Backend
- FastAPI + Jinja2
- Server-rendered HTML
- Static asset handling

## Unit Tests
- Route availability test
- End to end application flow tests
- Uses pytest + FastAPI TestClient

## Tech Stack
- Backend - FastAPI (Python 3.14)
- Templates - Jinja2
- FrontEnd - HTML + CSS
- Testing - Pytest
- Deployment - Render

## API Documentation
- POST /application
    Accepts the user input, parses it, then computes the output and renders output HTML file
