# app/data.py

skills = {
    "API Security": {
        "learning_time_months": 0.5,
        "prerequisites": ["REST APIs"],
        "recommended_resources": ["OWASP API Security Top 10"],
        "reason_to_learn": "Protects APIs from common vulnerabilities",
        "primary_focus": "Backend"
    },
    "AWS": {
        "learning_time_months": 2,
        "prerequisites": ["Linux Basics", "Networking Basics"],
        "recommended_resources": ["AWS Cloud Practitioner"],
        "reason_to_learn": "Cloud deployment and scalability",
        "primary_focus": "DevOps"
    },
    "Agile Methodology": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Scrum Guide"],
        "reason_to_learn": "Improves team-based software delivery",
        "primary_focus": "Process"
    },
    "Architecture Patterns": {
        "learning_time_months": 1,
        "prerequisites": ["System Design"],
        "recommended_resources": ["Design Patterns – GoF"],
        "reason_to_learn": "Reusable system-level solutions",
        "primary_focus": "Backend"
    },
    "Authentication": {
        "learning_time_months": 0.5,
        "prerequisites": ["REST APIs"],
        "recommended_resources": ["Auth0 Docs"],
        "reason_to_learn": "User identity management",
        "primary_focus": "Backend"
    },
    "Authorization": {
        "learning_time_months": 0.5,
        "prerequisites": ["Authentication"],
        "recommended_resources": ["OAuth.net"],
        "reason_to_learn": "Access control mechanisms",
        "primary_focus": "Backend"
    },
    "Bash": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Linux Command Line Basics"],
        "reason_to_learn": "Automation and system control",
        "primary_focus": "DevOps"
    },
    "Browser Internals": {
        "learning_time_months": 0.5,
        "prerequisites": ["JavaScript"],
        "recommended_resources": ["Google Developers"],
        "reason_to_learn": "Understand client-side execution",
        "primary_focus": "Frontend"
    },
    "CI/CD": {
        "learning_time_months": 1,
        "prerequisites": ["Git"],
        "recommended_resources": ["GitHub Actions Docs"],
        "reason_to_learn": "Automates testing and deployment",
        "primary_focus": "DevOps"
    },
    "CSS": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["MDN CSS"],
        "reason_to_learn": "Styling web applications",
        "primary_focus": "Frontend"
    },
    "Caching": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Web Caching Strategies"],
        "reason_to_learn": "Improves performance",
        "primary_focus": "Backend"
    },
    "Clean Architecture": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["Clean Architecture – Robert C. Martin"],
        "reason_to_learn": "Builds maintainable systems",
        "primary_focus": "Backend"
    },
    "Code Optimization": {
        "learning_time_months": 0.5,
        "prerequisites": ["Data Structures"],
        "recommended_resources": ["Performance Engineering Blogs"],
        "reason_to_learn": "Efficient runtime and memory usage",
        "primary_focus": "Fundamentals"
    },
    "Computer Networks": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["Computer Networking – Kurose"],
        "reason_to_learn": "Understanding data communication",
        "primary_focus": "Fundamentals"
    },
    "Concurrency": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["Concurrency in Practice"],
        "reason_to_learn": "Parallel task handling",
        "primary_focus": "Backend"
    },
    "Data Structures": {
        "learning_time_months": 1.5,
        "prerequisites": [],
        "recommended_resources": ["CLRS", "Striver A2Z"],
        "reason_to_learn": "Core problem-solving foundation",
        "primary_focus": "Fundamentals"
    },
    "Design Patterns": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["Refactoring Guru"],
        "reason_to_learn": "Reusable coding solutions",
        "primary_focus": "Backend"
    },
    "Distributed Systems": {
        "learning_time_months": 2,
        "prerequisites": ["System Design"],
        "recommended_resources": ["Designing Data-Intensive Applications"],
        "reason_to_learn": "Build scalable systems",
        "primary_focus": "Backend"
    },
    "Docker": {
        "learning_time_months": 1,
        "prerequisites": ["Linux Basics"],
        "recommended_resources": ["Docker Official Docs"],
        "reason_to_learn": "Containerized deployments",
        "primary_focus": "DevOps"
    },
    "Error Handling": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Clean Code"],
        "reason_to_learn": "Reliable applications",
        "primary_focus": "Backend"
    },
    "Express.js": {
        "learning_time_months": 0.5,
        "prerequisites": ["JavaScript"],
        "recommended_resources": ["Express Docs"],
        "reason_to_learn": "Backend web framework",
        "primary_focus": "Backend"
    },
    "FastAPI": {
        "learning_time_months": 0.5,
        "prerequisites": ["Python"],
        "recommended_resources": ["FastAPI Docs"],
        "reason_to_learn": "High-performance Python APIs",
        "primary_focus": "Backend"
    },
    "Git": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Git SCM"],
        "reason_to_learn": "Version control",
        "primary_focus": "Tools"
    },
    "Graph Algorithms": {
        "learning_time_months": 1,
        "prerequisites": ["Data Structures"],
        "recommended_resources": ["CP Algorithms"],
        "reason_to_learn": "Advanced problem-solving",
        "primary_focus": "Fundamentals"
    },
    "GraphQL": {
        "learning_time_months": 1,
        "prerequisites": ["REST APIs"],
        "recommended_resources": ["GraphQL Docs"],
        "reason_to_learn": "Flexible API querying",
        "primary_focus": "Backend"
    },
    "HTML": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["MDN HTML"],
        "reason_to_learn": "Structure of the web",
        "primary_focus": "Frontend"
    },
    "HTTP Protocol": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["MDN HTTP"],
        "reason_to_learn": "Web communication basics",
        "primary_focus": "Backend"
    },
    "JavaScript": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["JavaScript.info"],
        "reason_to_learn": "Core web language",
        "primary_focus": "Frontend"
    },
    "Kubernetes": {
        "learning_time_months": 2,
        "prerequisites": ["Docker"],
        "recommended_resources": ["Kubernetes Docs"],
        "reason_to_learn": "Container orchestration",
        "primary_focus": "DevOps"
    },
    "Linux Basics": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Linux Journey"],
        "reason_to_learn": "Server environments",
        "primary_focus": "Fundamentals"
    },
    "Load Balancing": {
        "learning_time_months": 0.5,
        "prerequisites": ["Networking Basics"],
        "recommended_resources": ["NGINX Docs"],
        "reason_to_learn": "Traffic distribution",
        "primary_focus": "DevOps"
    },
    "Logging": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Logging Best Practices"],
        "reason_to_learn": "Debugging and monitoring",
        "primary_focus": "Backend"
    },
    "Message Queues": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["RabbitMQ Docs"],
        "reason_to_learn": "Async communication",
        "primary_focus": "Backend"
    },
    "Microservices": {
        "learning_time_months": 1.5,
        "prerequisites": ["REST APIs"],
        "recommended_resources": ["Microservices Patterns"],
        "reason_to_learn": "Scalable systems",
        "primary_focus": "Backend"
    },
    "MongoDB": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["MongoDB University"],
        "reason_to_learn": "NoSQL databases",
        "primary_focus": "Database"
    },
    "Networking Basics": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Cisco Networking Basics"],
        "reason_to_learn": "Foundational networking",
        "primary_focus": "Fundamentals"
    },
    "Nginx": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Nginx Docs"],
        "reason_to_learn": "Web server and reverse proxy",
        "primary_focus": "DevOps"
    },
    "Node.js": {
        "learning_time_months": 0.5,
        "prerequisites": ["JavaScript"],
        "recommended_resources": ["Node.js Docs"],
        "reason_to_learn": "Backend runtime",
        "primary_focus": "Backend"
    },
    "OAuth": {
        "learning_time_months": 0.5,
        "prerequisites": ["API Security"],
        "recommended_resources": ["OAuth.net"],
        "reason_to_learn": "Secure authentication",
        "primary_focus": "Backend"
    },
    "Object-Oriented Design": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["OOD Principles"],
        "reason_to_learn": "Modular code design",
        "primary_focus": "Fundamentals"
    },
    "Performance Testing": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["JMeter Docs"],
        "reason_to_learn": "System benchmarking",
        "primary_focus": "Testing"
    },
    "PostgreSQL": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["PostgreSQL Tutorial"],
        "reason_to_learn": "Relational databases",
        "primary_focus": "Database"
    },
    "Problem Solving": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["Competitive Programming"],
        "reason_to_learn": "Analytical thinking",
        "primary_focus": "Fundamentals"
    },
    "Python": {
        "learning_time_months": 1,
        "prerequisites": [],
        "recommended_resources": ["Python Docs"],
        "reason_to_learn": "Backend and scripting",
        "primary_focus": "Backend"
    },
    "Queue Data Structures": {
        "learning_time_months": 0.5,
        "prerequisites": ["Data Structures"],
        "recommended_resources": ["GeeksForGeeks"],
        "reason_to_learn": "Core DS concepts",
        "primary_focus": "Fundamentals"
    },
    "Rate Limiting": {
        "learning_time_months": 0.5,
        "prerequisites": ["REST APIs"],
        "recommended_resources": ["System Design Primer"],
        "reason_to_learn": "Prevent abuse",
        "primary_focus": "Backend"
    },
    "React": {
        "learning_time_months": 1,
        "prerequisites": ["JavaScript"],
        "recommended_resources": ["React Docs"],
        "reason_to_learn": "Frontend UI development",
        "primary_focus": "Frontend"
    },
    "Redis": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Redis Docs"],
        "reason_to_learn": "In-memory caching",
        "primary_focus": "Database"
    },
    "REST APIs": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["RESTful API Design"],
        "reason_to_learn": "API architecture",
        "primary_focus": "Backend"
    },
    "Scalability Concepts": {
        "learning_time_months": 1,
        "prerequisites": ["System Design"],
        "recommended_resources": ["High Scalability Blog"],
        "reason_to_learn": "Handle growth",
        "primary_focus": "Backend"
    },
    "Search Algorithms": {
        "learning_time_months": 0.5,
        "prerequisites": ["Data Structures"],
        "recommended_resources": ["CLRS"],
        "reason_to_learn": "Efficient searching",
        "primary_focus": "Fundamentals"
    },
    "Software Testing": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Testing Pyramid"],
        "reason_to_learn": "Code correctness",
        "primary_focus": "Testing"
    },
    "Sorting Algorithms": {
        "learning_time_months": 0.5,
        "prerequisites": ["Data Structures"],
        "recommended_resources": ["Striver A2Z"],
        "reason_to_learn": "Core algorithm skills",
        "primary_focus": "Fundamentals"
    },
    "State Management": {
        "learning_time_months": 0.5,
        "prerequisites": ["React"],
        "recommended_resources": ["Redux Docs"],
        "reason_to_learn": "UI data consistency",
        "primary_focus": "Frontend"
    },
    "System Design": {
        "learning_time_months": 2,
        "prerequisites": ["Data Structures"],
        "recommended_resources": ["Grokking System Design"],
        "reason_to_learn": "Design large-scale systems",
        "primary_focus": "Backend"
    },
    "Technical Documentation": {
        "learning_time_months": 0.25,
        "prerequisites": [],
        "recommended_resources": ["Google Tech Writing"],
        "reason_to_learn": "Knowledge sharing",
        "primary_focus": "Process"
    },
    "Testing Automation": {
        "learning_time_months": 0.5,
        "prerequisites": ["Software Testing"],
        "recommended_resources": ["Cypress Docs"],
        "reason_to_learn": "Automated QA",
        "primary_focus": "Testing"
    },
    "TypeScript": {
        "learning_time_months": 0.5,
        "prerequisites": ["JavaScript"],
        "recommended_resources": ["TypeScript Docs"],
        "reason_to_learn": "Type-safe JavaScript",
        "primary_focus": "Frontend"
    },
    "Versioning Strategies": {
        "learning_time_months": 0.25,
        "prerequisites": ["Git"],
        "recommended_resources": ["Semantic Versioning"],
        "reason_to_learn": "Release management",
        "primary_focus": "Tools"
    },
    "Web Performance Optimization": {
        "learning_time_months": 0.5,
        "prerequisites": ["Browser Internals"],
        "recommended_resources": ["Web.dev"],
        "reason_to_learn": "Fast user experience",
        "primary_focus": "Frontend"
    },
    "Web Security": {
        "learning_time_months": 0.5,
        "prerequisites": ["HTTP Protocol"],
        "recommended_resources": ["OWASP Top 10"],
        "reason_to_learn": "Prevent common attacks",
        "primary_focus": "Security"
    },
    "WebSockets": {
        "learning_time_months": 0.5,
        "prerequisites": ["JavaScript"],
        "recommended_resources": ["WebSocket MDN"],
        "reason_to_learn": "Real-time communication",
        "primary_focus": "Backend"
    },
    "Workflow Orchestration": {
        "learning_time_months": 0.5,
        "prerequisites": [],
        "recommended_resources": ["Airflow Docs"],
        "reason_to_learn": "Task automation",
        "primary_focus": "DevOps"
    }
}

roles = {
    "Frontend Developer": {
        "level": 2,
        "experience_years": [0, 2],
        "skillset": ["HTML", "CSS", "JavaScript", "TypeScript", "React", "State Management"]
    },
    "Backend Developer": {
        "level": 2,
        "experience_years": [0, 2],
        "skillset": ["Python", "REST APIs", "PostgreSQL", "Error Handling", "FastAPI", "API Security"]
    },
    "Full Stack Developer": {
        "level": 3,
        "experience_years": [0, 2],
        "skillset": ["HTML", "CSS", "JavaScript", "Python", "REST APIs", "PostgreSQL", "React", "FastAPI"]
    },
    "DevOps Engineer": {
        "level": 3,
        "experience_years": [1, 3],
        "skillset": ["Linux Basics", "Bash", "Networking Basics", "Docker", "CI/CD", "AWS"]
    },
    "Software Engineer": {
        "level": 3,
        "experience_years": [1, 3],
        "skillset": ["Data Structures", "Problem Solving", "Computer Networks", "Git", "Python", "REST APIs"]
    },
    "Senior Backend Developer": {
        "level": 4,
        "experience_years": [3, 5],
        "skillset": ["Python", "REST APIs", "PostgreSQL", "Redis", "FastAPI", "System Design", "Scalability Concepts"]
    },
    "Senior Frontend Developer": {
        "level": 4,
        "experience_years": [3, 5],
        "skillset": ["JavaScript", "HTML", "CSS", "TypeScript", "React", "Browser Internals", "Web Performance Optimization"]
    },
    "Senior Full Stack Developer": {
        "level": 5,
        "experience_years": [4, 6],
        "skillset": ["JavaScript", "Python", "REST APIs", "PostgreSQL", "Redis", "React", "FastAPI", "Docker", "System Design"]
    },
    "Cloud Engineer": {
        "level": 4,
        "experience_years": [3, 5],
        "skillset": ["Linux Basics", "Networking Basics", "AWS", "Docker", "CI/CD", "Load Balancing"]
    },
    "Platform Engineer": {
        "level": 5,
        "experience_years": [4, 6],
        "skillset": ["Linux Basics", "Networking Basics", "Docker", "Kubernetes", "CI/CD", "System Design"]
    },
    "Site Reliability Engineer": {
        "level": 5,
        "experience_years": [4, 6],
        "skillset": ["Linux Basics", "Networking Basics", "Logging", "Docker", "AWS", "System Design"]
    },
    "API Engineer": {
        "level": 4,
        "experience_years": [3, 5],
        "skillset": ["REST APIs", "Python", "FastAPI", "API Security", "Rate Limiting", "OAuth"]
    },
    "Data Engineer": {
        "level": 4,
        "experience_years": [3, 5],
        "skillset": ["Python", "PostgreSQL", "MongoDB", "Message Queues", "Distributed Systems"]
    },
    "System Engineer": {
        "level": 4,
        "experience_years": [3, 5],
        "skillset": ["Linux Basics", "Computer Networks", "Nginx", "Load Balancing", "System Design"]
    },
    "Technical Architect": {
        "level": 6,
        "experience_years": [6, 100],
        "skillset": ["Clean Architecture", "Microservices", "Distributed Systems", "Architecture Patterns", "System Design"]
    }
}

levelTransitions = [
    {"level_difference": 1, "success_rate_percent": 85, "avg_transition_time_months": 4},
    {"level_difference": 2, "success_rate_percent": 70, "avg_transition_time_months": 7},
    {"level_difference": 3, "success_rate_percent": 55, "avg_transition_time_months": 10},
    {"level_difference": 4, "success_rate_percent": 40, "avg_transition_time_months": 14}
]
