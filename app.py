
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Career Recommendation System",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# CAREER DATABASE
# --------------------------------------------------

career_data = {
    "Programming": {
        "careers": [
            {
                "title": "Software Developer",
                "salary": "₹6-18 LPA",
                "demand": 95
            },
            {
                "title": "Python Developer",
                "salary": "₹5-15 LPA",
                "demand": 90
            },
            {
                "title": "AI/ML Engineer",
                "salary": "₹10-30 LPA",
                "demand": 98
            }
        ],
        "skills": [
            "Python",
            "DSA",
            "React",
            "Git",
            "System Design"
        ],
        "roadmap": [
            "Learn Programming Fundamentals",
            "Build Projects",
            "Practice DSA",
            "Open Source Contribution",
            "Apply for Jobs"
        ]
    },

    "Data Science": {
        "careers": [
            {
                "title": "Data Scientist",
                "salary": "₹8-25 LPA",
                "demand": 96
            },
            {
                "title": "ML Engineer",
                "salary": "₹10-30 LPA",
                "demand": 98
            },
            {
                "title": "Data Analyst",
                "salary": "₹5-15 LPA",
                "demand": 90
            }
        ],
        "skills": [
            "Python",
            "Statistics",
            "SQL",
            "Pandas",
            "Machine Learning"
        ],
        "roadmap": [
            "Learn Python",
            "Statistics",
            "Data Analysis",
            "Machine Learning",
            "Build Portfolio"
        ]
    },

    "Cyber Security": {
        "careers": [
            {
                "title": "Security Analyst",
                "salary": "₹6-20 LPA",
                "demand": 97
            },
            {
                "title": "Penetration Tester",
                "salary": "₹8-22 LPA",
                "demand": 92
            },
            {
                "title": "Cloud Security Engineer",
                "salary": "₹10-28 LPA",
                "demand": 95
            }
        ],
        "skills": [
            "Linux",
            "Networking",
            "Ethical Hacking",
            "Cloud",
            "Security Tools"
        ],
        "roadmap": [
            "Networking Basics",
            "Linux",
            "Cyber Security Fundamentals",
            "Ethical Hacking",
            "Certifications"
        ]
    },

    "UI/UX Design": {
        "careers": [
            {
                "title": "UI Designer",
                "salary": "₹5-16 LPA",
                "demand": 88
            },
            {
                "title": "UX Designer",
                "salary": "₹6-18 LPA",
                "demand": 90
            },
            {
                "title": "Product Designer",
                "salary": "₹8-22 LPA",
                "demand": 92
            }
        ],
        "skills": [
            "Figma",
            "Adobe XD",
            "Wireframing",
            "Research",
            "Prototyping"
        ],
        "roadmap": [
            "Learn Design Principles",
            "Master Figma",
            "Build Portfolio",
            "Case Studies",
            "Apply for Design Roles"
        ]
    }
}

# --------------------------------------------------
# SCORING FUNCTION
# --------------------------------------------------

def calculate_score(cgpa, skills, experience):

    score = 40

    cgpa_score = {
        "<6": 0,
        "6-7": 5,
        "7-8": 10,
        "8-9": 15,
        "9+": 20
    }

    exp_score = {
        "None": 0,
        "Internship": 8,
        "Projects": 10,
        "Freelancing": 12
    }

    score += cgpa_score[cgpa]
    score += exp_score[experience]

    score += min(len(skills) * 3, 20)

    return min(score, 100)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀 Smart Career Recommendation System")
st.write("AI-based Career Guidance for Engineering Students")

# --------------------------------------------------
# USER FORM
# --------------------------------------------------

with st.form("career_form"):

    st.subheader("Student Profile")

    name = st.text_input("Name")

    branch = st.selectbox(
        "Branch",
        [
            "Computer Science",
            "Information Technology",
            "Electronics",
            "Mechanical",
            "Civil",
            "Electrical"
        ]
    )

    year = st.selectbox(
        "Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]
    )

    cgpa = st.selectbox(
        "CGPA Range",
        [
            "<6",
            "6-7",
            "7-8",
            "8-9",
            "9+"
        ]
    )

    interest = st.selectbox(
        "Interest Area",
        list(career_data.keys())
    )

    skills = st.multiselect(
        "Current Skills",
        [
            "Python",
            "Java",
            "C++",
            "SQL",
            "React",
            "Linux",
            "Cloud",
            "Figma",
            "Machine Learning"
        ]
    )

    experience = st.selectbox(
        "Experience",
        [
            "None",
            "Internship",
            "Projects",
            "Freelancing"
        ]
    )

    submit = st.form_submit_button("Analyze Career")

# --------------------------------------------------
# RESULT
# --------------------------------------------------

if submit:

    score = calculate_score(
        cgpa,
        skills,
        experience
    )

    st.success(f"Career Fit Score: {score}%")

    domain = career_data[interest]

    st.subheader("Recommended Careers")

    df = pd.DataFrame(domain["careers"])
    st.dataframe(df, use_container_width=True)

    st.subheader("Skills You Should Learn")

    for skill in domain["skills"]:
        st.write("✅", skill)

    st.subheader("Career Roadmap")

    for i, step in enumerate(domain["roadmap"], start=1):
        st.write(f"{i}. {step}")

    st.subheader("Personalized Feedback")

    if score >= 85:
        st.success(
            "Excellent profile. You are highly competitive."
        )

    elif score >= 70:
        st.info(
            "Good profile. Focus on projects and internships."
        )

    else:
        st.warning(
            "Build more skills and practical experience."
        )

    st.balloons()