import streamlit as st
import json
from pathlib import Path

from agent.agent import agent_step  # or run_agent_step if that’s your name

if "page" not in st.session_state:
    st.session_state.page = "Home"


STATE_PATH = Path(__file__).parent / "state.json"



def load_state():
    with open(STATE_PATH, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

st.set_page_config(
    page_title="Kaya — Agentic Health Companion",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)
PRIMARY = "#948979"     # soft indigo
BG = "#222831"           # deep navy
CARD = "#696053"
TEXT = "#ffffff"
MUTED = "#9CA3AF"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Glass+Antiqua&family=Uncial+Antiqua&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Glass+Antiqua&family=Space+Grotesk:wght@300..700&family=Uncial+Antiqua&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Glass+Antiqua&family=Poiret+One&family=Space+Grotesk:wght@300..700&family=Uncial+Antiqua&display=swap');


.stApp {{
    background-color: {BG};
    color: {TEXT};
}}

/* BODY TEXT */
p, li, div {{
    font-family: Space Grotesk, serif !important;
    color: {TEXT};
}}

/* MAIN TITLE */
h1 {{
    font-family: 'Uncial Antiqua', serif !important;
    letter-spacing: 0.09em;
    font-size:4.5rem !important;
    text-align : center;
}}

/* SECTION HEADERS */
h2{{
    font-family: 'Glass Antiqua' , serif !important;
    
}}
h3 {{
    font-family: 'Glass Antiqua', serif !important;
    font-size:4rem !important;
}}

/* HANDWRITTEN / ACCENT TEXT */
.muted {{
    font-family: 'Caveat', cursive !important;
    color: {MUTED};
    font-size: 1.1rem;
}}

/* Cards */
.card {{
    background-color: {CARD};
    padding: 1.3rem;
    border-radius: 14px;
    margin-bottom: 1rem;
    border: 1px solid #1F2937;
}}


/* Buttons */
.stButton > button {{
    background-color: #948979;
    color: white;
    border-radius: 18px;

    /* SIZE CONTROL */
    padding: 1.2rem 2rem;    
    font-size: 1.5rem;        /* ⬅️ bigger text */
    font-weight: 600;

    width: 100%;              /* full-width buttons */
    height: auto;

    border: none;
    transition: all 0.15s ease-in-out;
    transform: scale(1.03);
    background-color: #7F7465;
}}
.center {{
    text-align: center;
    font-family: Poriet One, serif !important;
}}

.stButton > button:hover {{
    background-color: #DFD0B8;
}}
</style>
""", unsafe_allow_html=True)


state = load_state()

st.sidebar.title("Kaya")

page = st.sidebar.radio(
    "",
    ["Home", "Workout", "Diet", "Feedback"],
    index=["Home", "Workout", "Diet", "Feedback"].index(st.session_state.page)
)

st.session_state.page = page

if st.session_state.page == "Home":
    st.title("Kaya")
    st.markdown(
        "<p class='muted center'>Your adaptive health companion</p>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

if st.button("Home",icon="🏡",use_container_width=True):
    st.session_state.page = "Home"
    st.rerun()

if st.button("Workout", icon="🏋️‍♀️",use_container_width=True):
    st.session_state.page = "Workout"
    st.rerun()

if st.button("🥗 Diet", use_container_width=True):
    st.session_state.page = "Diet"
    st.rerun()

if st.button("📝 Feedback", use_container_width=True):
    st.session_state.page = "Feedback"
    st.rerun()

# ------------------------
# Current Plan Display
# ------------------------

diet = state["current_plan"]["diet_plan"]
exercise = state["current_plan"]["exercise"]

if st.session_state.page == "Diet":
    st.subheader("🥗 Diet Plan")

    diet = state["current_plan"]["diet_plan"]

    st.markdown(f"- **Carbs:** {diet['carbs']}")
    st.markdown(f"- **Fats:** {diet['fats']}")
    st.markdown(f"- **Protein:** {diet['protein']}")
    st.markdown(f"- **Fiber:** {diet['fiber']}")
    st.markdown(f"- **Other:** {', '.join(diet['other_micronutrients'])}")

if st.session_state.page == "Workout":
    st.subheader("🏋️ Workout Plan")

    exercise = state["current_plan"]["exercise"]

    st.markdown(f"**Duration:** {exercise['duration_minutes']} minutes")
    st.markdown(f"**Routine:** {exercise['routine']}")
    st.markdown(f"**Change:** {exercise['change']}")

# ------------------------
# Daily Check-in
# ------------------------
if st.session_state.page == "Feedback":
    st.subheader("📝 Daily Check-in")
    st.markdown("<p class='muted'>How are you feeling today?</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        energy = st.selectbox("Energy level", ["", "low", "normal", "high"])

    with col2:
        hunger = st.selectbox("Hunger level", ["", "low", "normal", "high"])

    if st.button("Submit Feedback"):
        state["progress"]["reported_energy_level"] = energy
        state["progress"]["overall_hunger"] = hunger

        save_state(state)
        new_state = agent_step()

        st.success("Plan updated!")

        with st.expander("🧠 Agent reasoning"):
            st.write(new_state["agent_meta"]["last_decision"])
            st.write(new_state["agent_meta"]["last_reasoning_summary"])

st.markdown(
    "<p class='muted' style='text-align:center;'>Powered by Kaya — made with love by the autobots</p>",
    unsafe_allow_html=True
)