import streamlit as st


def initialize_session_state():

    defaults = {
        # -----------------------------
        # Decision
        # -----------------------------
        "decision_question": "",
        "decision_goal": "",
        "uploaded_image": None,
    "camera_image": None,
    "voice_input": None,
    "user_context": "",
        # -----------------------------
        # Evidence
        # -----------------------------
        "uploaded_data": None,
        "vision_data": None,
        "voice_context": "",

        # -----------------------------
        # Gemini Analysis
        # -----------------------------
        "analysis_result": None,
        "analysis_complete": False,

        # -----------------------------
        # Decision Engine
        # -----------------------------
        "decision_score": None,
        "recommendation": None,
        "risk_level": None,
        "decision_factors": None,

        # -----------------------------
        # What-If Simulator
        # -----------------------------
        "scenario_score": None,
        "scenario_difference": None,
        "scenario_type": None,
        "scenario_history": [],
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value