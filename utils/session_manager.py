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
        "voice_transcript": "",
        "user_context": "",
        "scenario_used": False,
        "brief_viewed": False,

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
        "decision_factors": {},

        # -----------------------------
        # What-If Simulator
        # -----------------------------
        "scenario_score": None,
        "scenario_difference": None,
        "scenario_type": None,
        "scenario_history": [],
    }

    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

    st.session_state.setdefault("confirm_reset", False)