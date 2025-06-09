import streamlit as st

st.set_page_config(page_title="Personality Quiz", layout="centered")
st.title("🧠 Personality Quiz")

st.write("Answer these fun questions to find out your personality type!")

# Initialize session state for storing score
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Questions and options
questions = [
    {
        "question": "1. What's your ideal weekend?",
        "options": {
            "Reading a book 📚": 1,
            "Going to a party 🎉": 3,
            "Hiking in nature 🌳": 2,
            "Watching Netflix 🍿": 2
        }
    },
    {
        "question": "2. How do you handle stress?",
        "options": {
            "Talk it out with a friend 🗣️": 3,
            "Write in a journal 📝": 1,
            "Go for a run 🏃": 2,
            "Sleep it off 😴": 2
        }
    },
    {
        "question": "3. Which animal do you relate to?",
        "options": {
            "Owl 🦉": 1,
            "Tiger 🐅": 3,
            "Dog 🐶": 2,
            "Cat 🐱": 2
        }
    }
]

# Display questions
if not st.session_state.submitted:
    for i, q in enumerate(questions):
        st.markdown(f"**{q['question']}**")
        choice = st.radio("", list(q["options"].keys()), key=f"q{i}")

    if st.button("Submit Quiz"):
        total_score = 0
        for i, q in enumerate(questions):
            answer = st.session_state[f"q{i}"]
            total_score += q["options"][answer]
        st.session_state.score = total_score
        st.session_state.submitted = True
        st.rerun()  # ✅ Updated here
else:
    score = st.session_state.score
    st.markdown("### 🎉 Your Personality Type:")

    if score <= 4:
        st.success("**The Thoughtful Introvert** 🌙\n\nYou enjoy peace, deep thoughts, and quiet time.")
    elif 5 <= score <= 6:
        st.success("**The Balanced Explorer** 🌤️\n\nYou love a bit of adventure but also value rest.")
    else:
        st.success("**The Energetic Extrovert** 🔥\n\nYou're outgoing, expressive, and love excitement!")

    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.submitted = False
        st.rerun()  # ✅ Updated here too


