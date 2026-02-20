import streamlit as st

# --- 1. Mock Database of Careers ---
# In a real-world scenario, this would be connected to an API or a SQL database.
CAREER_DATA = {
    "Software Engineer": {
        "description": "Build applications, systems, and software.",
        "required_skills": ["Python", "Java", "JavaScript", "SQL", "Git", "Problem Solving", "Data Structures"],
        "roadmap": [
            "1. Master Python or Java syntax and basic logic.",
            "2. Learn Object-Oriented Programming (OOP).",
            "3. Understand Data Structures and Algorithms.",
            "4. Build a full-stack project (e.g., Django + React).",
            "5. Contribute to open source and prepare for technical interviews."
        ]
    },
    "Data Scientist": {
        "description": "Analyze data to derive insights and build predictive models.",
        "required_skills": ["Python", "Statistics", "Machine Learning", "SQL", "Data Visualization", "Pandas"],
        "roadmap": [
            "1. Learn Python and Pandas for data manipulation.",
            "2. Study Statistics and Linear Algebra.",
            "3. Complete courses on Scikit-Learn and TensorFlow.",
            "4. Analyze 3 real-world datasets and create visualizations.",
            "5. Build a portfolio of Machine Learning projects."
        ]
    },
    "UX/UI Designer": {
        "description": "Design user-friendly interfaces and experiences.",
        "required_skills": ["Figma", "Prototyping", "Wireframing", "User Research", "CSS", "Empathy"],
        "roadmap": [
            "1. Learn design principles (Color theory, Typography).",
            "2. Master Figma or Sketch for prototyping.",
            "3. Conduct user research and create personas.",
            "4. Design a complete mobile app or website.",
            "5. Create a Behance/Dribbble portfolio."
        ]
    },
    "Product Manager": {
        "description": "Guide the development and success of a product.",
        "required_skills": ["Communication", "Agile", "Roadmapping", "User Stories", "Analytics", "Leadership"],
        "roadmap": [
            "1. Understand the product lifecycle (Introduction to Growth).",
            "2. Learn Agile and Scrum methodologies.",
            "3. Practice writing effective User Stories and acceptance criteria.",
            "4. Analyze market competition and write a PRD (Product Requirement Document).",
            "5. Lead a mock product launch project."
        ]
    },
    "Digital Marketer": {
        "description": "Promote brands and products online.",
        "required_skills": ["SEO", "Content Writing", "Social Media", "Analytics", "Email Marketing"],
        "roadmap": [
            "1. Learn the basics of SEO and SEM.",
            "2. Get certified in Google Analytics.",
            "3. Create a content strategy for a mock brand.",
            "4. Manage a social media campaign.",
            "5. Analyze the results and optimize."
        ]
    }
}

# --- 2. Streamlit App Layout ---
def main():
    st.set_page_config(page_title="Career Guidance Bot", page_icon="🤖", layout="wide")

    # Sidebar: User Profile
    st.sidebar.title("👤 Your Profile")
    st.sidebar.write("Let's find the perfect career for you.")
    
    name = st.sidebar.text_input("Your Name", "User")
    
    # Input: Interests
    interest = st.sidebar.selectbox(
        "Which field interests you most?",
        ["Software Engineering", "Data Science", "Design", "Management", "Marketing"]
    )

    # Input: Current Skills (Multiselect)
    all_possible_skills = [
        "Python", "Java", "JavaScript", "SQL", "Git", "Statistics", 
        "Machine Learning", "Figma", "Prototyping", "Communication", 
        "Agile", "SEO", "Content Writing", "Excel", "Data Visualization"
    ]
    user_skills = st.sidebar.multiselect("Select skills you already have:", all_possible_skills)

    # Input: Experience
    experience = st.sidebar.radio("Current Experience Level:", 
                                  ["Student/Beginner", "Junior (1-3 Years)", "Mid-Level (3-5 Years)", "Senior (5+ Years)"])

    st.sidebar.markdown("---")
    analyze_btn = st.sidebar.button("Analyze Profile")

    # --- 3. Main Chat Interface ---
    st.title("💼 Career Path Recommender")
    st.write("Welcome! I am your virtual career assistant. Adjust your profile in the sidebar to get started.")

    if analyze_btn:
        # Logic: Map interest to a career (Simplified for demo)
        # In a complex app, we would use NLP or a scoring system
        if interest == "Software Engineering":
            target_career = "Software Engineer"
        elif interest == "Data Science":
            target_career = "Data Scientist"
        elif interest == "Design":
            target_career = "UX/UI Designer"
        elif interest == "Management":
            target_career = "Product Manager"
        else:
            target_career = "Digital Marketer"

        career_info = CAREER_DATA[target_career]
        required = set(career_info["required_skills"])
        current = set(user_skills)
        
        # Calculate Skill Gaps
        missing_skills = required - current

        # --- Display Results ---
        st.success(f"👋 Hello {name}, based on your interest in **{interest}**, we recommend: ** {target_career} **")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Your Current Skills")
            if current:
                for skill in current:
                    st.write(f"- {skill}")
            else:
                st.info("You haven't selected any skills yet.")

        with col2:
            st.subheader("🎯 Skills Needed")
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"- 🔴 **{skill}** (Gap)")
            else:
                st.balloons()
                st.write("You have all the required skills for this role!")

        # Roadmap
        st.divider()
        st.subheader("🗺️ Your Personalized Learning Roadmap")
        roadmap = career_info["roadmap"]
        for step in roadmap:
            st.write(step)

        # --- Chatbot Simulation ---
        st.divider()
        st.subheader("💬 Ask the Assistant")
        
        query = st.text_input(f"Ask a question about the {target_career} role:", 
                              placeholder="e.g., What is the average salary?")
        
        if query:
            q = query.lower()
            if "salary" in q:
                st.write(f"💰 Salaries for **{target_career}** vary by location, but typically range from **$60k to $150k** depending on experience.")
            elif "job" in q or "market" in q:
                st.write("📈 The job market is growing steadily! Tech and Data roles are in high demand.")
            elif "skill" in q:
                st.write("🤖 Hard skills (coding/design) are important, but soft skills like communication are often the differentiator.")
            else:
                st.write("🤖 That's a great question. I recommend checking out specific job listings on LinkedIn to see exact requirements!")

    else:
        # Default message when app loads
        st.info("Please fill out your profile in the sidebar and click 'Analyze Profile'.")
        
        # Display generic options just for UI visuals
        st.subheader("Popular Careers")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("**Software Engineer**\n\nBuild the future.")
        with c2:
            st.info("**Data Scientist**\n\nUncover insights.")
        with c3:
            st.info("**Product Manager**\n\nLead the vision.")

if __name__ == "__main__":
    main()