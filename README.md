# ◉ DeciScope

### AI-Powered Decision Intelligence Workspace

> **Turn scattered evidence into structured decisions.**

DeciScope is a multimodal AI-powered decision intelligence application built with **Python, Streamlit, Pandas, Plotly, and Google Gemini**.

It helps users evaluate real-world decisions by combining **text, workload data, images, camera input, and voice context** into a structured analysis.

Instead of simply asking an AI for an answer, DeciScope guides the user through a complete decision workflow:

**Decision → Evidence → Analysis → Scenarios → Intelligence Report**

---

## 🚀 Live Application

### [Launch DeciScope](https://deciscope.streamlit.app/)

Deployed using **Streamlit Community Cloud**.

 ---

## 🏗️ System Architecture and Prompt Strategy

For the complete system architecture, data flow, modules, state management, and deployment architecture:

👉 [View Architecture Documentation](docs/architecture.md)

👉 [ View Prompt Strategy Documentation ](docs/prompt_strategy.md)

---

## ✨ Features

### 🧭 01 · Decision

Start by defining the decision you want to evaluate.

Users can provide:

- Decision question
- Primary goal
- Relevant context

Examples:

> Should I attend this hackathon?

> Should I take this internship?

> Should I commit to this project?

---

### 📊 02 · Evidence

Decisions become more reliable when they are supported by evidence.

DeciScope allows users to provide:

- CSV activity and workload data
- Written context
- Images
- Screenshots
- Camera input
- Voice context

Uploaded CSV files can be edited directly inside the application using an interactive `st.data_editor`.

---

### 🤖 03 · AI Decision Analysis

Gemini analyzes the decision together with the evidence provided by the user.

The analysis evaluates factors including:

- Career Value
- Skill Alignment
- Networking Value
- Time Fit
- Deadline Safety

These factors are used to generate:

**Decision Score → Recommendation → Risk Level**

The AI analysis is designed specifically around the user's decision context rather than functioning as a generic chatbot.

---

### 🔄 04 · Scenario Simulator

The **What-If Scenario Simulator** allows users to test how changing different conditions could affect the decision.

Users can adjust factors such as:

- Career Value
- Skill Alignment
- Networking Value
- Time Fit
- Deadline Safety

The application then compares the scenario with the original decision score.

This answers questions such as:

> "What if the time commitment becomes smaller?"

> "What if the career value is higher?"

> "Would my recommendation change?"

---

### 📑 05 · Intelligence Report

The final stage converts the analysis into a structured decision report.

The report brings together:

- Decision overview
- Decision score
- Recommendation
- Risk level
- Evidence analysis
- Decision factors
- Scenario comparison
- Decision-changing conditions
- Missing information

The generated report can also be downloaded for future reference.

---

# 🧠 Multimodal AI

DeciScope combines multiple forms of evidence instead of relying only on text.

| Input | Purpose |
|---|---|
| 📝 Text | Decision and personal context |
| 📊 CSV | Activity and workload analysis |
| 🖼️ Image | Visual evidence analysis |
| 📷 Camera | Real-world visual evidence |
| 🎙️ Audio | Natural voice context |
| 🤖 Gemini | AI-powered decision analysis |

This creates a single workspace where different types of evidence can contribute to the same decision.

---

# 📊 Data Visualization

DeciScope transforms uploaded activity data into interactive visual insights.

Current visualizations include:

- **Hours by Category**
- **Workload by Priority**
- **Daily Time Allocation**
- **Development Time Percentage**
- **High-Priority Activity Insights**

The application uses **Pandas** for data processing and **Plotly** for interactive visualization.

---

# 🛠️ Technology Stack

| Technology | Role |
|---|---|
| **Python** | Application logic |
| **Streamlit** | Web application and UI |
| **Google Gemini** | AI decision analysis |
| **Gemini Vision** | Image-based evidence analysis |
| **Gemini Audio** | Voice evidence processing |
| **Pandas** | Data processing |
| **Plotly** | Interactive charts |
| **Pillow** | Image processing |
| **Git & GitHub** | Version control |
| **Streamlit Community Cloud** | Deployment |

---

# 📁 Project Structure

```text
DeciScope/
│
├── app.py
├── gemini_service.py
├── prompts.py
├── utils.py
├── requirements.txt
├── README.md
├── architecture.md
│
└── assets/
    └── deciscope_logo.png
```

## Core Modules

### `app.py`

Main Streamlit application containing:

- Page navigation
- UI components
- Session state
- Decision workflow
- Evidence collection
- Scenario simulator
- Intelligence report

### `gemini_service.py`

Handles Gemini API interaction and multimodal analysis.

### `prompts.py`

Contains the structured prompts used to guide Gemini's decision analysis.

### `utils.py`

Contains supporting functions such as:

- Decision scoring
- Recommendation generation
- Risk calculation
- Data processing utilities

---

# 🧮 Decision Scoring

DeciScope evaluates a decision using five primary factors:

| Factor | Purpose |
|---|---|
| **Career Value** | Measures potential career benefit |
| **Skill Alignment** | Measures relevance to the user's skills and goals |
| **Networking Value** | Measures potential networking opportunities |
| **Time Fit** | Measures compatibility with available time |
| **Deadline Safety** | Measures deadline and workload risk |

These factors contribute to a decision score ranging from:

```text
0 ───────────────────────────── 100
Low                              High
```

The resulting score is used to determine the application's:

- **Recommendation**
- **Risk Level**
- **Scenario Comparison**

---

# 🔐 API Security

The Gemini API key is **not hard-coded into the application**.

For local development, configure the key using Streamlit secrets.

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

For deployment, the API key is stored securely using **Streamlit Community Cloud Secrets**.

> ⚠️ Never commit API keys, passwords, or other sensitive credentials to GitHub.

---

# ⚙️ Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/Gawandeepkaur20/DeciScope.git
cd DeciScope
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Gemini API

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

## 5. Start the Application

```bash
streamlit run app.py
```

The application will then be available through the Streamlit development server.

---


# 🎯 Design Philosophy

DeciScope follows one core principle:

> **AI should help users understand a decision, not blindly make the decision for them.**

The application separates the decision-making process into five stages:

```text
┌─────────────────────┐
│       Define        │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Collect Evidence   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       Analyze       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Test Scenarios    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       Review        │
└─────────────────────┘
```

This makes the reasoning process easier to understand, compare, and revisit.

---

# 💡 Why DeciScope?

Traditional AI interactions often look like:

```text
User → Question → AI → Answer
```

DeciScope takes a more structured approach:

```text
User
  ↓
Decision
  ↓
Evidence
  ├── Text
  ├── CSV
  ├── Image
  ├── Camera
  └── Voice
  ↓
Gemini Analysis
  ↓
Decision Factors
  ↓
Score + Risk + Recommendation
  ↓
What-If Scenarios
  ↓
Intelligence Report
```

The goal is to move from simple **AI answers** toward **AI-assisted decision intelligence**.

---

# 🌟 Key Highlights

- ✅ Multimodal Gemini integration
- ✅ Text, image and audio evidence
- ✅ CSV workload analysis
- ✅ Interactive `st.data_editor`
- ✅ Plotly data visualizations
- ✅ Dynamic KPI cards
- ✅ Decision scoring
- ✅ Risk assessment
- ✅ What-if scenario simulation
- ✅ Decision comparison
- ✅ Intelligence Report
- ✅ Downloadable report
- ✅ Streamlit session-state workflow
- ✅ Streamlit Cloud deployment
- ✅ Secure API key handling
- ✅ Production-oriented dashboard UI

---

# 🚧 Future Improvements

Potential future enhancements include:

- 📌 Decision history
- 📊 Multiple decision comparison
- 👤 Persistent user profiles
- 🔄 Advanced scenario modeling
- 📅 Decision timeline tracking
- 📥 Additional evidence sources
- 📈 Historical decision analytics
- 🧠 Personalized decision patterns
- 📑 Enhanced report customization

---

# 🎓 Project Context

**DeciScope** was developed as an **AI Capstone Project for MirAI School of Technology**.

The project focuses on combining:

**Artificial Intelligence + Multimodal Inputs + Data Visualization + Interactive UI + Decision Intelligence**

---

# 👩‍💻 Author

## Gawandeep Kaur

**B.Tech Computer Science & Engineering**

### Areas of Interest

- Artificial Intelligence
- Full-Stack Development
- Python
- AI-powered applications
- Practical software development

---

# ⭐ Support

If you find DeciScope useful or interesting, consider giving the repository a ⭐ on GitHub.

---

### Built with Python, Streamlit & Gemini

**DeciScope — Make better decisions with better evidence.**
## Core Modules

### `app.py`

Main Streamlit application containing:

- Page navigation
- UI components
- Session state
- Decision workflow
- Evidence collection
- Scenario simulator
- Intelligence report

### `gemini_service.py`

Handles Gemini API interaction and multimodal analysis.

### `prompts.py`

Contains the structured prompts used to guide Gemini's decision analysis.

### `utils.py`

Contains supporting functions such as:

- Decision scoring
- Recommendation generation
- Risk calculation
- Data processing utilities

---

# 🧮 Decision Scoring

DeciScope evaluates a decision using five primary factors:

| Factor | Purpose |
|---|---|
| **Career Value** | Measures potential career benefit |
| **Skill Alignment** | Measures relevance to the user's skills and goals |
| **Networking Value** | Measures potential networking opportunities |
| **Time Fit** | Measures compatibility with available time |
| **Deadline Safety** | Measures deadline and workload risk |

These factors contribute to a decision score ranging from:

```text
0 ───────────────────────────── 100
Low                              High
```

The resulting score is used to determine the application's:

- **Recommendation**
- **Risk Level**
- **Scenario Comparison**

---

# 🔐 API Security

The Gemini API key is **not hard-coded into the application**.

For local development, configure the key using Streamlit secrets.

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

For deployment, the API key is stored securely using **Streamlit Community Cloud Secrets**.

> ⚠️ Never commit API keys, passwords, or other sensitive credentials to GitHub.

---

# ⚙️ Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/Gawandeepkaur20/DeciScope.git
cd DeciScope
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Gemini API

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

## 5. Start the Application

```bash
streamlit run app.py
```

The application will then be available through the Streamlit development server.

---



# 🎯 Design Philosophy

DeciScope follows one core principle:

> **AI should help users understand a decision, not blindly make the decision for them.**

The application separates the decision-making process into five stages:

```text
┌─────────────────────┐
│       Define        │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Collect Evidence   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       Analyze       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Test Scenarios    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       Review        │
└─────────────────────┘
```

This makes the reasoning process easier to understand, compare, and revisit.

---

# 💡 Why DeciScope?

Traditional AI interactions often look like:

```text
User → Question → AI → Answer
```

DeciScope takes a more structured approach:

```text
User
  ↓
Decision
  ↓
Evidence
  ├── Text
  ├── CSV
  ├── Image
  ├── Camera
  └── Voice
  ↓
Gemini Analysis
  ↓
Decision Factors
  ↓
Score + Risk + Recommendation
  ↓
What-If Scenarios
  ↓
Intelligence Report
```

The goal is to move from simple **AI answers** toward **AI-assisted decision intelligence**.

---

# 🌟 Key Highlights

- ✅ Multimodal Gemini integration
- ✅ Text, image and audio evidence
- ✅ CSV workload analysis
- ✅ Interactive `st.data_editor`
- ✅ Plotly data visualizations
- ✅ Dynamic KPI cards
- ✅ Decision scoring
- ✅ Risk assessment
- ✅ What-if scenario simulation
- ✅ Decision comparison
- ✅ Intelligence Report
- ✅ Downloadable report
- ✅ Streamlit session-state workflow
- ✅ Streamlit Cloud deployment
- ✅ Secure API key handling
- ✅ Production-oriented dashboard UI

---

# 🚧 Future Improvements

Potential future enhancements include:

- 📌 Decision history
- 📊 Multiple decision comparison
- 👤 Persistent user profiles
- 🔄 Advanced scenario modeling
- 📅 Decision timeline tracking
- 📥 Additional evidence sources
- 📈 Historical decision analytics
- 🧠 Personalized decision patterns
- 📑 Enhanced report customization

---

# 🎓 Project Context

**DeciScope** was developed as an **AI Capstone Project for MirAI School of Technology**.

The project focuses on combining:

**Artificial Intelligence + Multimodal Inputs + Data Visualization + Interactive UI + Decision Intelligence**

---

# 👩‍💻 Author

## Gawandeep Kaur

**B.Tech Computer Science & Engineering**

### Areas of Interest

- Artificial Intelligence
- Full-Stack Development
- Python
- AI-powered applications
- Practical software development

---

# ⭐ Support

If you find DeciScope useful or interesting, consider giving the repository a ⭐ on GitHub.

---

### Built with Python, Streamlit & Gemini

**DeciScope — Make better decisions with better evidence.**


