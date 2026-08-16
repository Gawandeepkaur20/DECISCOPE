import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

from services.gemini_service import analyze_decision
from utils.data_processor import (
    process_uploaded_csv,
    validate_dataframe,
    prepare_dataframe,
    calculate_metrics
)
from utils.session_manager import initialize_session_state
from services.decision_engine import (
    calculate_decision_score,
    get_recommendation,
    get_risk_level
)
from services.scenario_engine import (
    calculate_scenario_score,
    compare_scores
)
def load_css():

    css_path = Path("styles.css")

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()
st.set_page_config(
    page_title="DeciScope",
    page_icon="DS",
    layout="wide"
)
# =========================================================
# DECISCOPE UI STYLING
# =========================================================


# =========================================================
# DECISCOPE UI
# =========================================================




initialize_session_state()
if "scenario_used" not in st.session_state:
    st.session_state.scenario_used = False

if "brief_viewed" not in st.session_state:
    st.session_state.brief_viewed = False
# =========================================================
# DECISCOPE — FINAL UI THEME
# =========================================================
# =========================================================
# DECISCOPE BACKGROUND ORBS
# =========================================================

st.markdown("""
<div class="deciscope-orb orb-one"></div>
<div class="deciscope-orb orb-two"></div>
<div class="deciscope-orb orb-three"></div>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* =========================================================
   1. GLOBAL APP
   ========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 85% 5%,
            rgba(99, 102, 241, 0.07),
            transparent 28%
        ),
        radial-gradient(
            circle at 10% 90%,
            rgba(148, 163, 184, 0.07),
            transparent 30%
        ),
        #F7F8FC;

    color: #111827;
}

/* =====================================================
   ANIMATED BACKGROUND ORBS
===================================================== */

.deciscope-orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    filter: blur(70px);
}

/* top-right */
.orb-one {
    width: 280px;
    height: 280px;
    right: 5%;
    top: 8%;
  background: rgba(99, 102, 241, 0.45);
    animation: orbMoveOne 16s ease-in-out infinite;
}

/* bottom-left */
.orb-two {
    width: 240px;
    height: 240px;
    left: 8%;
    bottom: 5%;
    background: rgba(148, 163, 184, 0.18);
    animation: orbMoveTwo 20s ease-in-out infinite;
}

/* middle */
.orb-three {
    width: 180px;
    height: 180px;
    left: 48%;
    top: 45%;
    background: rgba(129, 140, 248, 0.08);
    animation: orbMoveThree 24s ease-in-out infinite;
}


/* =====================================================
   ORB ANIMATIONS
===================================================== */

@keyframes orbMoveOne {

    0%, 100% {
        transform: translate(0px, 0px);
    }

    50% {
        transform: translate(-60px, 45px);
    }

}

@keyframes orbMoveTwo {

    0%, 100% {
        transform: translate(0px, 0px);
    }

    50% {
        transform: translate(55px, -45px);
    }

}

@keyframes orbMoveThree {

    0%, 100% {
        transform: translate(0px, 0px);
    }

    50% {
        transform: translate(-35px, 30px);
    }

}

/* =========================================================
   3. MAIN CONTENT
   ========================================================= */

.main .block-container {

    padding-top: 2.5rem;
    padding-bottom: 4rem;

    position: relative;
    z-index: 1;

    animation:
        deciPageIn
        0.35s
        ease-out;
}


@keyframes deciPageIn {

    from {
        opacity: 0;
        transform: translateY(6px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* =========================================================
   4. TYPOGRAPHY
   ========================================================= */

h1 {
    color: #111827 !important;

    font-weight: 700 !important;

    letter-spacing: -0.8px;
}


h2 {
    color: #111827 !important;

    font-weight: 650 !important;

    letter-spacing: -0.5px;
}


h3 {
    color: #111827 !important;

    font-weight: 600 !important;
}


p {
    color: #1F2937;
}


/* =========================================================
   5. CAPTIONS — DARK
   ========================================================= */

[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {

    color: #111827 !important;

    opacity: 1 !important;
}


/* =========================================================
   6. SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {

    background: #F3F4F6 !important;

    border-right:
        1px solid #E1E4E8 !important;

    position: relative;

    z-index: 2;
}


section[data-testid="stSidebar"] > div {

    background: #F3F4F6 !important;

    padding-top: 1.5rem;
}


/* Sidebar headings */

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {

    color: #111827 !important;
}


/* Sidebar normal text */

section[data-testid="stSidebar"] p {

    color: #1F2937 !important;
}


/* Sidebar captions */

section[data-testid="stSidebar"]
[data-testid="stCaptionContainer"] p {

    color: #374151 !important;
}


/* =========================================================
   7. SIDEBAR WORKSPACE NAVIGATION
   ========================================================= */

section[data-testid="stSidebar"]
div[role="radiogroup"]
label {

    background: transparent !important;

    color: #111827 !important;

    border-radius: 10px !important;

    border-left:
        3px solid transparent !important;

    padding:
        9px 12px !important;

    margin:
        3px 0 !important;

    transition:
        background 0.2s ease,
        border-color 0.2s ease;
}


/* Navigation text */

section[data-testid="stSidebar"]
div[role="radiogroup"]
label p {

    color: #111827 !important;
}


/* ACTIVE ITEM */

section[data-testid="stSidebar"]
div[role="radiogroup"]
label:has(input:checked) {

    background: #E1E4E8 !important;

    border-left:
        3px solid #9CA3AF !important;
}


/* Active text */

section[data-testid="stSidebar"]
div[role="radiogroup"]
label:has(input:checked) p {

    color: #111827 !important;

    font-weight: 600 !important;
}


/* Hover */

section[data-testid="stSidebar"]
div[role="radiogroup"]
label:hover {

    background: #E8EAED !important;
}


/* Radio accent */

section[data-testid="stSidebar"]
div[role="radiogroup"]
label input {

    accent-color: #6B7280 !important;
}


/* Remove focus glow */

section[data-testid="stSidebar"]
div[role="radiogroup"]
label:has(input:focus) {

    box-shadow: none !important;
}


/* =========================================================
   8. CARDS
   ========================================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        rgba(255, 255, 255, 0.92) !important;

    border:
        1px solid #E4E7EC !important;

    border-radius:
        16px !important;

    box-shadow:
        0 5px 20px
        rgba(25, 30, 50, 0.04);
}


/* =========================================================
   9. BUTTONS
   ========================================================= */

.stButton > button {

    border-radius:
        10px !important;

    border:
        1px solid #D1D5DB !important;

    background:
        #FFFFFF !important;

   

    font-weight:
        550 !important;

    padding:
        0.55rem 1.1rem !important;

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease,
        background 0.18s ease;
}


.stButton > button:hover {

    transform:
        translateY(-1px);

    background:
        #F3F4F6 !important;

    border-color:
        #9CA3AF !important;

    box-shadow:
        0 5px 15px
        rgba(25, 30, 50, 0.08);
}


/* Primary button */

.stButton > button[kind="primary"] {

    background:
        #374151 !important;

    color:
        #FFFFFF !important;

    border:
        none !important;
}


.stButton > button[kind="primary"]:hover {

    background:
        #1F2937 !important;

    box-shadow:
        0 7px 18px
        rgba(31, 41, 55, 0.18);
}


/* =========================================================
   10. TEXT INPUTS
   ========================================================= */

.stTextInput input,
.stTextArea textarea {

    border-radius:
        10px !important;

    border:
        1px solid #DDE1E7 !important;

    background:
        #FFFFFF !important;

    color:
        #111827 !important;
}


.stTextInput input:focus,
.stTextArea textarea:focus {

    border-color:
        #9CA3AF !important;

    box-shadow:
        0 0 0 2px
        rgba(107, 114, 128, 0.10) !important;
}


/* =========================================================
   11. SELECTBOX
   ========================================================= */

.stSelectbox div[data-baseweb="select"] {

    border-radius:
        10px !important;

    background:
        #FFFFFF !important;
}


/* =========================================================
   12. METRICS
   ========================================================= */

div[data-testid="stMetric"] {

    background:
        rgba(255, 255, 255, 0.92);

    border:
        1px solid #E4E7EC;

    border-radius:
        14px;

    padding:
        16px 18px;

    box-shadow:
        0 4px 15px
        rgba(20, 25, 40, 0.035);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}


div[data-testid="stMetric"]:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 8px 22px
        rgba(20, 25, 40, 0.07);
}


/* =========================================================
   13. EXPANDERS
   ========================================================= */

div[data-testid="stExpander"] {

    border:
        1px solid #E1E4E8 !important;

    border-radius:
        12px !important;

    background:
        #FFFFFF !important;

    overflow:
        hidden;
}


div[data-testid="stExpander"] summary:hover {

    background:
        #F3F4F6 !important;
}


/* =========================================================
   14. FILE UPLOADER
   ========================================================= */

section[data-testid="stFileUploaderDropzone"] {

    border:
        1px dashed #C7CBD3 !important;

    border-radius:
        14px !important;

    background:
        #FAFAFB !important;
}


section[data-testid="stFileUploaderDropzone"]:hover {

    border-color:
        #9CA3AF !important;

    background:
        #F5F6F7 !important;
}


/* =========================================================
   15. ALERTS
   ========================================================= */

div[data-testid="stAlert"] {

    border-radius:
        12px !important;
}


/* =========================================================
   16. DIVIDERS
   ========================================================= */

hr {

    border:
        none !important;

    border-top:
        1px solid #E1E4E8 !important;

    margin:
        1.5rem 0;
}


/* =========================================================
   17. PLOTLY
   ========================================================= */

.js-plotly-plot {

    border-radius:
        14px;

    overflow:
        hidden;
}


/* =========================================================
   18. MOBILE
   ========================================================= */

@media (max-width: 768px) {

    .main .block-container {

        padding-left:
            1rem;

        padding-right:
            1rem;

        padding-top:
            1.5rem;
    }


    h1 {

        font-size:
            1.8rem !important;
    }
}

</style>
""", unsafe_allow_html=True)
# =========================================================
# FORM SUBMIT BUTTON — DECISCOPE
# =========================================================

st.markdown("""
<style>

/* Analyze Decision / all form submit buttons */
div[data-testid="stFormSubmitButton"] > button {
    background-color: #E5E7EB !important;
    color: #111827 !important;
    border: 1px solid #D1D5DB !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    min-height: 44px !important;
    transition: all 0.2s ease !important;
}

/* Hover */
div[data-testid="stFormSubmitButton"] > button:hover {
    background-color: #D1D5DB !important;
    color: #111827 !important;
    border-color: #9CA3AF !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* Click */
div[data-testid="stFormSubmitButton"] > button:active {
    background-color: #CBD5E1 !important;
    transform: translateY(0);
}

/* Button text */
div[data-testid="stFormSubmitButton"] > button p {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* Disabled state */
div[data-testid="stFormSubmitButton"] > button:disabled {
    background-color: #E5E7EB !important;
    color: #6B7280 !important;
    opacity: 1 !important;
}

div[data-testid="stFormSubmitButton"] > button:disabled p {
    color: #6B7280 !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

button[kind="secondary"] {
    background: #E5E7EB !important;
    color: #374151 !important;
    border: 1px solid #D1D5DB !important;
}

button[kind="secondary"]:hover {
    background: #D1D5DB !important;
    color: #111827 !important;
}

</style>
""", unsafe_allow_html=True)
# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    # ------------------------------------------
    # BRAND
    # ------------------------------------------

    st.markdown("## DeciScope")

    st.caption(
        "Decision intelligence workspace"
    )

    st.divider()

    # ------------------------------------------
    # WORKSPACE NAVIGATION
    # ------------------------------------------

    st.markdown("### WORKSPACE")

   # =========================================================
# WORKSPACE NAVIGATION
# =========================================================

    completed_decision = bool(
        st.session_state.decision_question
    )

    completed_evidence = bool(
        st.session_state.uploaded_data is not None
        or st.session_state.vision_data is not None
        or st.session_state.voice_context
    )

    completed_analysis = bool(
        st.session_state.analysis_complete
    )

    page = st.radio(
        "Navigate",
        [
            "Decision",
            "Evidence",
            "Analysis",
            "Scenarios",
            "Decision Brief"
        ],
        label_visibility="collapsed"
    )
    
    st.divider()

    # ------------------------------------------
    # CURRENT DECISION
    # ------------------------------------------

    st.markdown("### CURRENT DECISION")

    if st.session_state.decision_question:

        st.caption(
            st.session_state.decision_question
        )

        if st.session_state.analysis_complete:

            st.success(
                "✓ Analysis ready"
            )

        else:

            st.caption(
                "Analysis not completed"
            )

    else:

        st.caption(
            "No decision started yet."
        )

    st.divider()

    # ------------------------------------------
    # EVIDENCE STATUS
    # ------------------------------------------

    st.markdown("### EVIDENCE")

    evidence_count = 0

    # Activity data
    if st.session_state.uploaded_data is not None:

        st.write("✓ Activity data")

        evidence_count += 1

    else:

        st.caption("○ Activity data")

    # Visual evidence
    if (
        st.session_state.get("uploaded_image") is not None
        or
        st.session_state.get("camera_image") is not None
        or
        st.session_state.get("vision_data") is not None
    ):

        st.write("✓ Visual evidence")

        evidence_count += 1

    else:

        st.caption("○ Visual evidence")

    # Voice evidence
    if st.session_state.get("voice_input") is not None:

        st.write("✓ Voice context")

        evidence_count += 1

    else:

        st.caption("○ Voice context")

    st.caption(
        f"{evidence_count} evidence source"
        f"{'s' if evidence_count != 1 else ''} added"
    )

    st.divider()

    # ------------------------------------------
    # ANALYSIS STATUS
    # ------------------------------------------

    st.markdown("### ANALYSIS STATUS")

    if st.session_state.analysis_complete:

        st.success(
            "Decision analysis complete"
        )

        score = st.session_state.get(
            "decision_score"
        )

        if score is not None:

            st.metric(
                "Decision Score",
                f"{score}/100"
            )

    else:

        st.info(
            "Analysis pending"
        )

    st.divider()

    # ------------------------------------------
# WORKFLOW PROGRESS
# ------------------------------------------

    st.markdown("### WORKFLOW")

    # 01 Decision
    if st.session_state.decision_question:
        st.write("✓ 01  Decision")
    else:
        st.caption("○ 01  Decision")


    # 02 Evidence
    if evidence_count > 0:
        st.write("✓ 02  Evidence")
    else:
        st.caption("○ 02  Evidence")


    # 03 Analysis
    if st.session_state.analysis_complete:
        st.write("✓ 03  Analysis")
    else:
        st.caption("○ 03  Analysis")


    # 04 Scenarios
    if st.session_state.scenario_used:
        st.write("✓ 04  Scenarios")
    elif st.session_state.analysis_complete:
        st.info("→ 04  Scenarios")
    else:
        st.caption("○ 04  Scenarios")


    # 05 Decision Brief
    if st.session_state.brief_viewed:
        st.write("✓ 05  Decision Brief")
    elif st.session_state.analysis_complete:
        st.info("→ 05  Decision Brief")
    else:
        st.caption("○ 05  Decision Brief")
        
    st.divider()

    if st.button(
        "↻  Start New Decision",
        use_container_width=True
    ):
        # Decision
        st.session_state.decision_question = ""
        st.session_state.decision_goal = ""

        # Evidence
        st.session_state.uploaded_data = None
        st.session_state.user_context = ""
        st.session_state.uploaded_image = None
        st.session_state.camera_image = None
        st.session_state.voice_input = None
        st.session_state.vision_data = None

        # Analysis
        st.session_state.analysis_result = None
        st.session_state.analysis_complete = False
        st.session_state.decision_factors = {}
        st.session_state.decision_score = None
        st.session_state.recommendation = None
        st.session_state.risk_level = None

        # Scenarios
        st.session_state.scenario_used = False

        # Decision Brief
        st.session_state.brief_viewed = False

        # Reset scenario sliders
        for key in [
            "scenario_career_value",
            "scenario_skill_alignment",
            "scenario_networking_value",
            "scenario_time_fit",
            "scenario_deadline_safety"
        ]:
            st.session_state.pop(key, None)

        st.success("Ready for a new decision.")

        st.rerun()   
    # ------------------------------------------
    # FOOTER
    # ------------------------------------------

    st.caption(
        "DeciScope • Evidence-based decisions"
    )
# -----------------------------
# Header
# -----------------------------

st.title("DeciScope")

st.caption(
    "Decision intelligence for choices that actually matter."
)




# -----------------------------
# Decision Input
# -----------------------------

st.divider()

# =========================================================
# 01 · DECISION
# =========================================================

# =========================================================
# 01 · DECISION COCKPIT
# =========================================================

if page == "Decision":

    st.caption("01 / 05  •  DECISION COCKPIT")

    st.title("Make the decision clear.")

    st.caption(
        "Define the choice first. DeciScope will turn your evidence "
        "into a structured decision view."
    )

    st.write("")

    # =====================================================
    # DECISION INPUT
    # =====================================================

    with st.container(border=True):

        st.caption("DECISION DEFINITION")

        st.subheader("What are you deciding?")

        st.caption(
            "Describe the choice you are currently considering."
        )

        with st.form("decision_form"):

            decision_question = st.text_input(
                "Decision",
                placeholder=(
                    "e.g. Should I attend this hackathon?"
                ),
                label_visibility="collapsed"
            )

            st.write("")

            decision_goal = st.selectbox(
                "Primary goal",
                [
                    "Career Growth",
                    "Learning",
                    "Time Management",
                    "Financial Value",
                    "Personal Development"
                ]
            )

            st.write("")

            submitted = st.form_submit_button(
                "Create Decision →",
                use_container_width=True
            )

    # =====================================================
    # SAVE DECISION
    # =====================================================

    if submitted:

        if not decision_question.strip():

            st.warning(
                "Enter a decision before continuing."
            )

        else:

            st.session_state.decision_question = (
                decision_question.strip()
            )

            st.session_state.decision_goal = (
                decision_goal
            )

            st.session_state.analysis_complete = False

            st.success(
                "Decision created. Continue to Evidence."
            )

    # =====================================================
    # DECISION STATUS
    # =====================================================

    if st.session_state.decision_question:

        st.write("")
        st.divider()

        st.caption("CURRENT DECISION")

        st.subheader(
            st.session_state.decision_question
        )

        st.caption(
            f"Primary goal · "
            f"{st.session_state.decision_goal}"
        )

        st.write("")

        # -------------------------------------------------
        # STATUS CARDS
        # -------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Decision",
                "Defined"
            )

        with col2:

            evidence_count = (
                int(
                    st.session_state.uploaded_data
                    is not None
                )
                +
                int(
                    st.session_state.vision_data
                    is not None
                )
                +
                int(
                    bool(
                        st.session_state.voice_context
                    )
                )
            )

            st.metric(
                "Evidence",
                f"{evidence_count}/3"
            )

        with col3:

            if st.session_state.analysis_complete:

                st.metric(
                    "Analysis",
                    "Ready"
                )

            else:

                st.metric(
                    "Analysis",
                    "Pending"
                )

        st.write("")

        # -------------------------------------------------
        # NEXT STEP
        # -------------------------------------------------

        if not st.session_state.analysis_complete:

            st.info(
                "Next step: add evidence to make the decision "
                "analysis more reliable."
            )

        else:

            st.success(
                "Decision analysis is ready. "
                "Review your Decision Brief."
            )
# =========================================================
# 02 · EVIDENCE FIELD
# =========================================================

if page == "Evidence":

    st.caption("02 / 05  •  EVIDENCE FIELD")

    st.title("Build the evidence.")

    st.caption(
        "Give DeciScope the context, data and visual information "
        "needed to understand your decision."
    )

    st.write("")

    # =====================================================
    # EVIDENCE STATUS
    # =====================================================

    data_ready = st.session_state.uploaded_data is not None
    image_ready = (
        st.session_state.uploaded_image is not None
        or st.session_state.camera_image is not None
    )
    voice_ready = st.session_state.voice_input is not None
    context_ready = bool(
        st.session_state.get("user_context", "").strip()
    )

    
    st.divider()

    # =====================================================
    # ACTIVITY DATA
    # =====================================================

    st.caption("01  ·  ACTIVITY DATA")

    with st.container(border=True):

        st.subheader("Activity & workload")

        st.caption(
            "Upload structured information about your time, "
            "workload and priorities."
        )

        uploaded_file = st.file_uploader(
            "Upload activity data",
            type=["csv"],
            help="CSV containing date, category, hours and priority."
        )

        if uploaded_file is not None:

            try:

                data = pd.read_csv(uploaded_file)

                st.session_state.uploaded_data = data

                st.success(
                    f"Loaded {len(data)} activity records."
                )

            except Exception as error:

                st.error(
                    f"Unable to read the CSV file: {error}"
                )

        data = st.session_state.get("uploaded_data")

        if data is not None:

            edited_df = st.data_editor(
                data,
                use_container_width=True,
                num_rows="dynamic"
            )

            st.session_state.uploaded_data = edited_df

            metrics = calculate_metrics(edited_df)

            # ---------------------------------------------
            # WORKLOAD SUMMARY
            # ---------------------------------------------

            metric1, metric2, metric3 = st.columns(3)

            with metric1:
                st.metric(
                    "Tracked Hours",
                    f"{metrics['total_hours']:.1f}"
                )

            with metric2:
                st.metric(
                    "Development Hours",
                    f"{metrics['development_hours']:.1f}"
                )

            with metric3:
                st.metric(
                    "High Priority",
                    metrics["high_priority"]
                )

            # ---------------------------------------------
            # ACTIVITY CHARTS
            # ---------------------------------------------

            st.write("")

            chart_col1, chart_col2 = st.columns(2)

            with chart_col1:

                category_data = (
                    edited_df
                    .groupby(
                        "category",
                        as_index=False
                    )["hours"]
                    .sum()
                )

                fig_category = px.bar(
                    category_data,
                    x="category",
                    y="hours",
                    title="Hours by Category"
                )

                st.plotly_chart(
                    fig_category,
                    use_container_width=True
                )

            with chart_col2:

                priority_data = (
                    edited_df
                    .groupby(
                        "priority",
                        as_index=False
                    )["hours"]
                    .sum()
                )

                fig_priority = px.pie(
                    priority_data,
                    names="priority",
                    values="hours",
                    title="Workload by Priority"
                )

                st.plotly_chart(
                    fig_priority,
                    use_container_width=True
                )

            daily_data = (
                edited_df
                .groupby(
                    "date",
                    as_index=False
                )["hours"]
                .sum()
            )

            fig_daily = px.line(
                daily_data,
                x="date",
                y="hours",
                markers=True,
                title="Daily Time Allocation"
            )

            st.plotly_chart(
                fig_daily,
                use_container_width=True
            )

    st.write("")

    # =====================================================
    # CONTEXT + VISUAL EVIDENCE
    # =====================================================

    context_col, visual_col = st.columns(2)

    # =====================================================
    # ADDITIONAL CONTEXT
    # =====================================================

    with context_col:

        st.caption("02  ·  CONTEXT")

        with st.container(border=True):

            st.subheader("What should DeciScope know?")

            st.caption(
                "Add information that may not appear in your data."
            )

            user_context = st.text_area(
                "Additional context",
                value=st.session_state.get(
                    "user_context",
                    ""
                ),
                placeholder=(
                    "Example: I have an assignment due Monday "
                    "and want to improve my AI skills."
                ),
                height=180,
                label_visibility="collapsed"
            )

            st.session_state.user_context = user_context

            if user_context.strip():

                st.success("Context added")

    # =====================================================
    # VISUAL EVIDENCE
    # =====================================================

    with visual_col:

        st.caption("03  ·  VISUAL EVIDENCE")

        with st.container(border=True):

            st.subheader("Add a visual")

            st.caption(
                "Upload a screenshot, schedule, document or photo."
            )

            visual_method = st.radio(
                "Evidence source",
                [
                    "Upload image",
                    "Take a photo"
                ],
                horizontal=True,
                key="visual_method"
            )

            if visual_method == "Upload image":

                uploaded_image = st.file_uploader(
                    "Choose an image",
                    type=[
                        "png",
                        "jpg",
                        "jpeg",
                        "webp"
                    ],
                    key="decision_image"
                )

                if uploaded_image is not None:

                    st.session_state.uploaded_image = uploaded_image
                    st.session_state.camera_image = None

                    
                    st.success("Visual evidence added")

            else:

                camera_image = st.camera_input(
                    "Take a photo",
                    key="decision_camera"
                )

                if camera_image is not None:

                    st.session_state.camera_image = camera_image
                    st.session_state.uploaded_image = None

                    # =========================================================
# DISPLAY SAVED VISUAL EVIDENCE
# =========================================================

                    saved_image = (
                        st.session_state.get("uploaded_image")
                        or
                        st.session_state.get("camera_image")
                    )

                    if saved_image is not None:

                        st.divider()

                        st.caption("ADDED VISUAL EVIDENCE")

                        
                        st.success(
                            "Visual evidence is ready for analysis."
                        )

                        st.write("")

    # =====================================================
    # VOICE CONTEXT
    # =====================================================

    st.caption("04  ·  VOICE CONTEXT")

    with st.container(border=True):

        st.subheader("Explain it naturally")

        st.caption(
            "Record your situation and let Gemini extract useful context."
        )

        voice_input = st.audio_input(
            "Record your context",
            key="decision_voice"
        )

        st.session_state.voice_input = voice_input

        if voice_input is not None:

            st.success("Voice context added")

    st.write("")

    # =====================================================
    # READY STATE
    # =====================================================

    evidence_count = sum([
        data_ready,
        image_ready,
        context_ready,
        voice_ready
    ])

    if evidence_count == 0:

        st.info(
            "Add at least one source of evidence before running analysis."
        )

    else:

        st.success(
            f"{evidence_count} evidence source"
            f"{'s' if evidence_count != 1 else ''} ready for analysis."
        )
    
# =========================================================
# 03 · ANALYSIS — AI INTELLIGENCE LAB
# =========================================================

if page == "Analysis":

    st.caption("03 · INTELLIGENCE LAB")
    st.title("Decision Analysis")

    st.caption(
        "DeciScope interprets the evidence and identifies the signals "
        "that matter to your decision."
    )

    # ---------------------------------------------------------
    # NO DECISION
    # ---------------------------------------------------------

    if not st.session_state.decision_question:

        st.info(
            "Create a decision first to begin the analysis."
        )

        st.stop()

    # ---------------------------------------------------------
    # DECISION CONTEXT
    # ---------------------------------------------------------

    with st.container(border=True):

        st.caption("CURRENT DECISION")

        st.markdown(
            f"### {st.session_state.decision_question}"
        )

        st.caption(
            f"Primary objective · {st.session_state.decision_goal}"
        )

    st.write("")

    # ---------------------------------------------------------
    # ANALYZE BUTTON
    # ---------------------------------------------------------

    if not st.session_state.analysis_complete:

        with st.container(border=True):

            st.markdown("### Run intelligence analysis")

            st.caption(
                "DeciScope will combine your decision, context, "
                "structured data, visual evidence and voice input."
            )

            st.write("")
            with st.form("ai_analysis_form"):

                analyze_clicked = st.form_submit_button(
            "Analyze Decision",
            use_container_width=True
        )

            if analyze_clicked:

                image = None

                uploaded_image = st.session_state.get(
                    "uploaded_image"
                )

                camera_image = st.session_state.get(
                    "camera_image"
                )

                if uploaded_image is not None:

                    from PIL import Image

                    image = Image.open(
                        uploaded_image
                    )

                elif camera_image is not None:

                    from PIL import Image

                    image = Image.open(
                        camera_image
                    )

                if image is not None:

                    st.session_state.vision_data = image

                data_context = ""

                if st.session_state.uploaded_data is not None:

                    data = st.session_state.uploaded_data

                    data_context = data.to_string(
                        index=False
                    )

                user_context = st.session_state.get(
                    "user_context",
                    ""
                )

                voice_input = st.session_state.get(
                    "voice_input"
                )

                with st.spinner(
                    "DeciScope is interpreting your evidence..."
                ):

                    try:

                        result = analyze_decision(

                            decision_question=(
                                st.session_state.decision_question
                            ),

                            decision_goal=(
                                st.session_state.decision_goal
                            ),

                            user_context=user_context,

                            image=image,

                            audio=voice_input,

                            data_context=data_context
                        )

                        # -------------------------------------
                        # SAVE RESULT
                        # -------------------------------------

                        st.session_state.analysis_result = result
                        st.session_state.analysis_complete = True

                        factors = result.get(
                            "decision_factors",
                            {}
                        )

                        score = calculate_decision_score(

                            career_value=factors.get(
                                "career_value",
                                0
                            ),

                            skill_alignment=factors.get(
                                "skill_alignment",
                                0
                            ),

                            networking_value=factors.get(
                                "networking_value",
                                0
                            ),

                            time_fit=factors.get(
                                "time_fit",
                                0
                            ),

                            deadline_safety=factors.get(
                                "deadline_safety",
                                0
                            )
                        )

                        recommendation = get_recommendation(
                            score
                        )

                        risk_level = get_risk_level(
                            score
                        )

                        st.session_state.decision_factors = factors

                        st.session_state.decision_score = score

                        st.session_state.recommendation = recommendation

                        st.session_state.risk_level = risk_level

                        st.rerun()

                    except Exception as error:

                        st.error(
                            f"Gemini analysis failed: {error}"
                        )

    # ---------------------------------------------------------
    # ANALYSIS RESULT
    # ---------------------------------------------------------

    if st.session_state.analysis_complete:

        result = st.session_state.analysis_result

        st.write("")

        # =====================================================
        # ANALYSIS OVERVIEW
        # =====================================================

        st.caption("AI INTERPRETATION")

        with st.container(border=True):

            st.subheader(
                "What the evidence suggests"
            )

            st.write(
                result.get(
                    "decision_summary",
                    "No summary was generated."
                )
            )

        st.write("")

        # =====================================================
        # VISUAL EVIDENCE
        # =====================================================

        vision_data = st.session_state.get(
            "vision_data"
        )

        if vision_data is not None:

            st.caption("VISUAL SIGNALS")

            with st.container(border=True):

                visual_col1, visual_col2 = st.columns(
                    [1, 1.25]
                )

                with visual_col1:

                    st.image(
                        vision_data,
                        use_container_width=True
                    )

                with visual_col2:

                    st.subheader(
                        "What DeciScope detected"
                    )

                    visual_evidence = result.get(
                        "visual_evidence",
                        []
                    )

                    if visual_evidence:

                        for item in visual_evidence:

                            st.markdown(
                                f"✓ {item}"
                            )

                    else:

                        st.caption(
                            "No decision-relevant visual signals "
                            "were identified."
                        )

        # =====================================================
        # EVIDENCE SIGNALS
        # =====================================================

        st.write("")

        st.caption("EVIDENCE SIGNALS")

        signal_col1, signal_col2 = st.columns(2)

        with signal_col1:

            with st.container(border=True):

                st.subheader("Benefits")

                benefits = result.get(
                    "benefits",
                    []
                )

                if benefits:

                    for item in benefits:

                        st.markdown(
                            f"✓ {item}"
                        )

                else:

                    st.caption(
                        "No benefits identified."
                    )

        with signal_col2:

            with st.container(border=True):

                st.subheader("Risks")

                risks = result.get(
                    "risks",
                    []
                )

                if risks:

                    for item in risks:

                        st.markdown(
                            f"⚠ {item}"
                        )

                else:

                    st.caption(
                        "No major risks identified."
                    )

        # =====================================================
        # DECISION UNCERTAINTY
        # =====================================================

        st.write("")

        uncertainty_col1, uncertainty_col2 = st.columns(2)

        with uncertainty_col1:

            with st.expander(
                "Constraints"
            ):

                constraints = result.get(
                    "constraints",
                    []
                )

                if constraints:

                    for item in constraints:

                        st.write(
                            "•",
                            item
                        )

                else:

                    st.caption(
                        "No constraints identified."
                    )

        with uncertainty_col2:

            with st.expander(
                "Missing information"
            ):

                missing = result.get(
                    "missing_information",
                    []
                )

                if missing:

                    for item in missing:

                        st.write(
                            "•",
                            item
                        )

                else:

                    st.success(
                        "No major missing information identified."
                    )

        # =====================================================
        # DECISION CHANGERS
        # =====================================================

        st.write("")

        with st.container(border=True):

            st.subheader(
                "What could change the decision?"
            )

            changers = result.get(
                "decision_changers",
                []
            )

            if changers:

                for item in changers:

                    st.markdown(
                        f"→ {item}"
                    )

            else:

                st.caption(
                    "No major decision-changing conditions identified."
                )

        # =====================================================
        # NEXT STEP
        # =====================================================

        st.write("")

        with st.container(border=True):

            st.markdown(
                "### Intelligence analysis complete"
            )

            st.caption(
                "Use Scenarios to test alternative conditions, "
                "or open Decision Brief for the final recommendation."
            )

            st.info(
                "Next → **Scenarios** or **Decision Brief**"
            )
# =========================================================
# 05 · INTELLIGENCE REPORT
# =========================================================

if page == "Decision Brief":

    st.caption("05 · INTELLIGENCE REPORT")
    st.header("Intelligence Report")

    st.caption(
        "A decision-ready summary generated from the evidence analyzed by DeciScope."
    )
    st.session_state.brief_viewed = True
    # ---------------------------------------------------------
    # CHECK ANALYSIS
    # ---------------------------------------------------------

    if not st.session_state.analysis_complete:

        st.info(
            "Complete the decision analysis first to generate your Intelligence Report."
        )

    else:

        result = st.session_state.analysis_result or {}

        # -----------------------------------------------------
        # CORE VALUES
        # -----------------------------------------------------

        score = st.session_state.get(
            "decision_score",
            0
        )

        recommendation = st.session_state.get(
            "recommendation",
            "Not available"
        )

        risk_level = st.session_state.get(
            "risk_level",
            "Not available"
        )

        decision_question = st.session_state.get(
            "decision_question",
            "Decision"
        )

        decision_goal = st.session_state.get(
            "decision_goal",
            "Not specified"
        )

        factors = result.get(
            "decision_factors",
            {}
        )

        # -----------------------------------------------------
        # REPORT HEADER
        # -----------------------------------------------------

        st.divider()

        st.markdown(
            f"## {decision_question}"
        )

        st.caption(
            f"Primary objective · {decision_goal}"
        )

        st.write("")

        # -----------------------------------------------------
        # KPI CARDS
        # -----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Decision Score",
                f"{score}/100"
            )

        with col2:

            st.metric(
                "Recommendation",
                recommendation
            )

        with col3:

            st.metric(
                "Risk Level",
                risk_level
            )

        # -----------------------------------------------------
        # EXECUTIVE ASSESSMENT
        # -----------------------------------------------------

        st.divider()

        st.caption("EXECUTIVE ASSESSMENT")

        st.subheader(
            "Decision Summary"
        )

        st.write(
            result.get(
                "decision_summary",
                "No summary available."
            )
        )

        # -----------------------------------------------------
        # DECISION PROFILE
        # -----------------------------------------------------

        if factors:

            st.divider()

            st.caption("DECISION PROFILE")

            st.subheader(
                "Evidence-weighted factors"
            )

            st.caption(
                "Relative strength of the factors used by the decision engine."
            )

            factor_labels = {
                "career_value": "Career Value",
                "skill_alignment": "Skill Alignment",
                "networking_value": "Networking Value",
                "time_fit": "Time Fit",
                "deadline_safety": "Deadline Safety"
            }

            factor_values = {
                label: int(
                    factors.get(key, 0)
                )
                for key, label in factor_labels.items()
            }

            # -------------------------------------------------
            # FACTOR METRICS
            # -------------------------------------------------

            factor_cols = st.columns(5)

            for col, (label, value) in zip(
                factor_cols,
                factor_values.items()
            ):

                with col:

                    st.metric(
                        label,
                        f"{value}/100"
                    )

            st.write("")

            # -------------------------------------------------
            # RADAR CHART
            # -------------------------------------------------

            import plotly.graph_objects as go

            categories = list(
                factor_values.keys()
            )

            values = list(
                factor_values.values()
            )

            categories_closed = (
                categories + [categories[0]]
            )

            values_closed = (
                values + [values[0]]
            )

            fig = go.Figure()

            fig.add_trace(
                go.Scatterpolar(
                    r=values_closed,
                    theta=categories_closed,
                    fill="toself",
                    name="Decision Profile"
                )
            )

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )
                ),
                showlegend=False,
                height=430,
                margin=dict(
                    l=50,
                    r=50,
                    t=40,
                    b=40
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # -----------------------------------------------------
        # EVIDENCE & BENEFITS
        # -----------------------------------------------------

        st.divider()

        st.caption("EVIDENCE & OPPORTUNITY")

        evidence_col, benefits_col = st.columns(2)

        with evidence_col:

            st.subheader("Evidence")

            evidence = result.get(
                "evidence",
                []
            )

            if evidence:

                for item in evidence:

                    st.markdown(
                        f"• {item}"
                    )

            else:

                st.caption(
                    "No evidence was identified."
                )

        with benefits_col:

            st.subheader("Benefits")

            benefits = result.get(
                "benefits",
                []
            )

            if benefits:

                for item in benefits:

                    st.markdown(
                        f"• {item}"
                    )

            else:

                st.caption(
                    "No benefits were identified."
                )

        # -----------------------------------------------------
        # RISKS & CONSTRAINTS
        # -----------------------------------------------------

        st.divider()

        st.caption("RISK & LIMITATIONS")

        risks_col, constraints_col = st.columns(2)

        with risks_col:

            st.subheader("Risks")

            risks = result.get(
                "risks",
                []
            )

            if risks:

                for item in risks:

                    st.markdown(
                        f"• {item}"
                    )

            else:

                st.caption(
                    "No major risks identified."
                )

        with constraints_col:

            st.subheader("Constraints")

            constraints = result.get(
                "constraints",
                []
            )

            if constraints:

                for item in constraints:

                    st.markdown(
                        f"• {item}"
                    )

            else:

                st.caption(
                    "No constraints identified."
                )

        # -----------------------------------------------------
        # DECISION CHANGERS
        # -----------------------------------------------------

        st.divider()

        with st.expander(
            "What could change this decision?"
        ):

            changers = result.get(
                "decision_changers",
                []
            )

            if changers:

                for item in changers:

                    st.markdown(
                        f"• {item}"
                    )

            else:

                st.caption(
                    "No major decision-changing factors identified."
                )

        # -----------------------------------------------------
        # MISSING INFORMATION
        # -----------------------------------------------------

        with st.expander(
            "Information still missing"
        ):

            missing = result.get(
                "missing_information",
                []
            )

            if missing:

                for item in missing:

                    st.markdown(
                        f"• {item}"
                    )

            else:

                st.success(
                    "The analysis contains sufficient information."
                )

        # =====================================================
        # PDF REPORT GENERATOR
        # =====================================================

        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            Table,
            TableStyle
        )
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.enums import TA_CENTER
        from io import BytesIO
        from datetime import datetime

        def build_pdf_report():

            buffer = BytesIO()

            document = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=45,
                leftMargin=45,
                topMargin=45,
                bottomMargin=45
            )

            styles = getSampleStyleSheet()

            title_style = styles["Title"]

            title_style.alignment = TA_CENTER

            heading_style = styles["Heading2"]

            body_style = styles["BodyText"]

            story = []

            # -------------------------------------------------
            # TITLE
            # -------------------------------------------------

            story.append(
                Paragraph(
                    "DECISCOPE",
                    title_style
                )
            )

            story.append(
                Paragraph(
                    "Decision Intelligence Report",
                    styles["Heading2"]
                )
            )

            story.append(
                Spacer(1, 15)
            )

            story.append(
                Paragraph(
                    f"<b>Decision:</b> {decision_question}",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Primary Goal:</b> {decision_goal}",
                    body_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Generated:</b> "
                    f"{datetime.now().strftime('%d %B %Y, %H:%M')}",
                    body_style
                )
            )

            story.append(
                Spacer(1, 20)
            )

            # -------------------------------------------------
            # SUMMARY TABLE
            # -------------------------------------------------

            summary_data = [
                [
                    "Decision Score",
                    "Recommendation",
                    "Risk Level"
                ],
                [
                    f"{score}/100",
                    str(recommendation),
                    str(risk_level)
                ]
            ]

            summary_table = Table(
                summary_data,
                colWidths=[
                    160,
                    160,
                    160
                ]
            )

            summary_table.setStyle(
                TableStyle([
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#E5E7EB")
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.HexColor("#D1D5DB")
                    ),
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, -1),
                        "Helvetica"
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        10
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        10
                    )
                ])
            )

            story.append(
                summary_table
            )

            story.append(
                Spacer(1, 20)
            )

            # -------------------------------------------------
            # EXECUTIVE ASSESSMENT
            # -------------------------------------------------

            story.append(
                Paragraph(
                    "Executive Assessment",
                    heading_style
                )
            )

            story.append(
                Paragraph(
                    result.get(
                        "decision_summary",
                        "No summary available."
                    ),
                    body_style
                )
            )

            story.append(
                Spacer(1, 15)
            )

            # -------------------------------------------------
            # FACTORS
            # -------------------------------------------------

            if factors:

                story.append(
                    Paragraph(
                        "Decision Factors",
                        heading_style
                    )
                )

                factor_data = [
                    [
                        "Factor",
                        "Score"
                    ]
                ]

                for label, value in factor_values.items():

                    factor_data.append(
                        [
                            label,
                            f"{value}/100"
                        ]
                    )

                factor_table = Table(
                    factor_data,
                    colWidths=[
                        360,
                        120
                    ]
                )

                factor_table.setStyle(
                    TableStyle([
                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, 0),
                            colors.HexColor("#E5E7EB")
                        ),
                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            0.5,
                            colors.HexColor("#D1D5DB")
                        ),
                        (
                            "ALIGN",
                            (1, 1),
                            (1, -1),
                            "CENTER"
                        ),
                        (
                            "TOPPADDING",
                            (0, 0),
                            (-1, -1),
                            7
                        ),
                        (
                            "BOTTOMPADDING",
                            (0, 0),
                            (-1, -1),
                            7
                        )
                    ])
                )

                story.append(
                    factor_table
                )

                story.append(
                    Spacer(1, 20)
                )

            # -------------------------------------------------
            # HELPER FOR LIST SECTIONS
            # -------------------------------------------------

            def add_list_section(
                title,
                items
            ):

                story.append(
                    Paragraph(
                        title,
                        heading_style
                    )
                )

                if items:

                    for item in items:

                        story.append(
                            Paragraph(
                                f"• {item}",
                                body_style
                            )
                        )

                        story.append(
                            Spacer(1, 4)
                        )

                else:

                    story.append(
                        Paragraph(
                            "None identified.",
                            body_style
                        )
                    )

                story.append(
                    Spacer(1, 12)
                )

            # -------------------------------------------------
            # REPORT SECTIONS
            # -------------------------------------------------

            add_list_section(
                "Evidence",
                result.get("evidence", [])
            )

            add_list_section(
                "Benefits",
                result.get("benefits", [])
            )

            add_list_section(
                "Risks",
                result.get("risks", [])
            )

            add_list_section(
                "Constraints",
                result.get("constraints", [])
            )

            add_list_section(
                "What Could Change This Decision",
                result.get("decision_changers", [])
            )

            add_list_section(
                "Information Still Missing",
                result.get("missing_information", [])
            )

            # -------------------------------------------------
            # FOOTER
            # -------------------------------------------------

            story.append(
                Spacer(1, 20)
            )

            story.append(
                Paragraph(
                    "Generated by DeciScope · Decision Intelligence Workspace",
                    body_style
                )
            )

            document.build(story)

            buffer.seek(0)

            return buffer

        # =====================================================
        # DOWNLOAD
        # =====================================================

        st.divider()

        st.caption("REPORT")

        st.subheader(
            "Export your decision intelligence"
        )

        st.caption(
            "Download a PDF containing the complete analysis."
        )

        pdf_file = build_pdf_report()

        st.download_button(
            label="↓  Download Intelligence Report",
            data=pdf_file,
            file_name="DeciScope_Intelligence_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )     
   # =========================================================
# 04 · SCENARIOS — SCENARIO SIMULATOR
# =========================================================

if page == "Scenarios":

    st.caption("04 · SCENARIO SIMULATOR")
    st.title("What if things changed?")

    st.caption(
        "Adjust the conditions and see how the decision responds."
    )

    # ---------------------------------------------------------
    # CHECK ANALYSIS
    # ---------------------------------------------------------

    decision_factors = st.session_state.get(
        "decision_factors"
    ) or {}

    if not decision_factors:

        with st.container(border=True):

            st.markdown("### Scenario analysis is locked")

            st.caption(
                "Complete the Decision Analysis first. "
                "Your original evidence-based factors will be used "
                "as the baseline."
            )

            st.info(
                "Next → Open **Analysis** from the sidebar."
            )

        st.stop()

    # ---------------------------------------------------------
    # ORIGINAL VALUES
    # ---------------------------------------------------------

    original_career_value = int(
        decision_factors.get("career_value", 0)
    )

    original_skill_alignment = int(
        decision_factors.get("skill_alignment", 0)
    )

    original_networking_value = int(
        decision_factors.get("networking_value", 0)
    )

    original_time_fit = int(
        decision_factors.get("time_fit", 0)
    )

    original_deadline_safety = int(
        decision_factors.get("deadline_safety", 0)
    )

    original_score = st.session_state.get(
        "decision_score"
    )

    if original_score is None:

        original_score = calculate_decision_score(
            career_value=original_career_value,
            skill_alignment=original_skill_alignment,
            networking_value=original_networking_value,
            time_fit=original_time_fit,
            deadline_safety=original_deadline_safety
        )

    # ---------------------------------------------------------
    # BASELINE
    # ---------------------------------------------------------

    st.caption("BASELINE")

    with st.container(border=True):

        baseline_col1, baseline_col2, baseline_col3 = st.columns(3)

        with baseline_col1:

            st.metric(
                "Current score",
                f"{original_score}/100"
            )

        with baseline_col2:

            st.metric(
                "Current recommendation",
                st.session_state.get(
                    "recommendation",
                    "—"
                )
            )

        with baseline_col3:

            st.metric(
                "Current risk",
                st.session_state.get(
                    "risk_level",
                    "—"
                )
            )

    st.write("")

    # =========================================================
    # SCENARIO CONTROLS
    # =========================================================

    st.caption("SCENARIO CONTROLS")

    with st.container(border=True):

        st.subheader("Change the conditions")

        st.caption(
            "Move a factor up or down to simulate a different situation."
        )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            scenario_career_value = st.slider(
                "Career Value",
                0,
                100,
                original_career_value,
                key="scenario_career_value"
            )

            scenario_skill_alignment = st.slider(
                "Skill Alignment",
                0,
                100,
                original_skill_alignment,
                key="scenario_skill_alignment"
            )

            scenario_networking_value = st.slider(
                "Networking Value",
                0,
                100,
                original_networking_value,
                key="scenario_networking_value"
            )

        with col2:

            scenario_time_fit = st.slider(
                "Time Fit",
                0,
                100,
                original_time_fit,
                key="scenario_time_fit"
            )

            scenario_deadline_safety = st.slider(
                "Deadline Safety",
                0,
                100,
                original_deadline_safety,
                key="scenario_deadline_safety"
            )

    # =========================================================
    # CALCULATE
    # =========================================================

    scenario_score = calculate_decision_score(
        career_value=scenario_career_value,
        skill_alignment=scenario_skill_alignment,
        networking_value=scenario_networking_value,
        time_fit=scenario_time_fit,
        deadline_safety=scenario_deadline_safety
    )
    # Mark scenario as completed
    st.session_state.scenario_used = True
    scenario_recommendation = get_recommendation(
        scenario_score
    )

    scenario_risk = get_risk_level(
        scenario_score
    )

    score_difference = (
        scenario_score - original_score
    )

    # =========================================================
    # SCENARIO RESULT
    # =========================================================

    st.write("")

    st.caption("SCENARIO RESULT")

    with st.container(border=True):

        result_col1, result_col2, result_col3 = st.columns(3)

        with result_col1:

            st.metric(
                "Scenario score",
                f"{scenario_score}/100",
                delta=score_difference
            )

        with result_col2:

            st.metric(
                "Recommendation",
                scenario_recommendation
            )

        with result_col3:

            st.metric(
                "Risk level",
                scenario_risk
            )

        st.write("")

        # -----------------------------------------------------
        # SCORE BAR
        # -----------------------------------------------------

        st.caption("Decision strength")

        st.progress(
            scenario_score / 100
        )

        st.write("")

        # -----------------------------------------------------
        # INTERPRETATION
        # -----------------------------------------------------

        if score_difference > 0:

            st.success(
                f"This scenario improves the decision by "
                f"{score_difference} points."
            )

        elif score_difference < 0:

            st.warning(
                f"This scenario reduces the decision score by "
                f"{abs(score_difference)} points."
            )

        else:

            st.info(
                "This scenario produces the same decision score "
                "as the baseline."
            )

    # =========================================================
    # ORIGINAL VS SCENARIO
    # =========================================================

    st.write("")

    st.caption("BASELINE VS SCENARIO")

    with st.container(border=True):

        comparison_col1, comparison_col2 = st.columns(2)

        with comparison_col1:

            st.subheader("Original")

            st.metric(
                "Score",
                f"{original_score}/100"
            )

            st.caption(
                "Evidence-based baseline"
            )

        with comparison_col2:

            st.subheader("Scenario")

            st.metric(
                "Score",
                f"{scenario_score}/100",
                delta=score_difference
            )

            st.caption(
                "Your simulated conditions"
            )

    # =========================================================
    # FACTOR CHANGES
    # =========================================================

    st.write("")

    st.caption("WHAT CHANGED?")

    factor_comparison = {
        "Career Value": (
            original_career_value,
            scenario_career_value
        ),
        "Skill Alignment": (
            original_skill_alignment,
            scenario_skill_alignment
        ),
        "Networking Value": (
            original_networking_value,
            scenario_networking_value
        ),
        "Time Fit": (
            original_time_fit,
            scenario_time_fit
        ),
        "Deadline Safety": (
            original_deadline_safety,
            scenario_deadline_safety
        )
    }

    with st.container(border=True):

        for label, values in factor_comparison.items():

            original_value, scenario_value = values

            difference = (
                scenario_value - original_value
            )

            factor_col1, factor_col2, factor_col3 = st.columns(
                [2, 1, 1]
            )

            with factor_col1:

                st.write(label)

            with factor_col2:

                st.write(
                    f"{original_value} → {scenario_value}"
                )

            with factor_col3:

                if difference > 0:

                    st.success(
                        f"+{difference}"
                    )

                elif difference < 0:

                    st.warning(
                        f"{difference}"
                    )

                else:

                    st.caption(
                        "No change"
                    )

    # =========================================================
    # DECISION IMPACT
    # =========================================================

    st.write("")

    with st.container(border=True):

        st.subheader("Scenario interpretation")

        if score_difference >= 10:

            st.markdown(
                "### Strong positive shift"
            )

            st.write(
                "The changed conditions substantially strengthen "
                "the case for this decision."
            )

        elif score_difference > 0:

            st.markdown(
                "### Positive shift"
            )

            st.write(
                "The changed conditions make the decision somewhat "
                "more favorable."
            )

        elif score_difference <= -10:

            st.markdown(
                "### Significant negative shift"
            )

            st.write(
                "The changed conditions materially weaken the "
                "case for this decision."
            )

        elif score_difference < 0:

            st.markdown(
                "### Negative shift"
            )

            st.write(
                "The changed conditions make the decision somewhat "
                "less favorable."
            )

        else:

            st.markdown(
                "### No meaningful shift"
            )

            st.write(
                "The changed conditions do not alter the overall "
                "decision score."
            )

    # =========================================================
    # NEXT STEP
    # =========================================================

    st.write("")

    with st.container(border=True):

        st.markdown("### Ready to make the call?")

        st.caption(
            "Review the final Decision Brief for the evidence-backed "
            "recommendation."
        )

        st.info(
            "Next → **Decision Brief**"
        )