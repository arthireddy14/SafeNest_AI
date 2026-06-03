import streamlit as st
import json
import os

st.title("🚨 Threat Analyzer")

# -----------------------------
# Read Vacation Mode Status
# -----------------------------

VACATION_FILE = "data/vacation_mode.json"

vacation_mode = False

if os.path.exists(VACATION_FILE):
    try:
        with open(VACATION_FILE, "r") as f:
            data = json.load(f)
            vacation_mode = data.get(
                "vacation_mode",
                False
            )
    except:
        vacation_mode = False

# -----------------------------
# Inputs
# -----------------------------

person = st.selectbox(
    "Person Detected",
    [
        "Known Person",
        "Unknown Person"
    ]
)

time_of_day = st.selectbox(
    "Time",
    [
        "Day",
        "Night"
    ]
)

event = st.multiselect(
    "Security Events",
    [
        "Door Opened",
        "Window Opened",
        "Motion Detected"
    ]
)

# -----------------------------
# Analyze Button
# -----------------------------

if st.button("Analyze Threat"):

    risk_score = 0

    # Person

    if person == "Unknown Person":
        risk_score += 40
    else:
        risk_score += 5

    # Time

    if time_of_day == "Night":
        risk_score += 25
    else:
        risk_score += 5

    # Events

    if "Door Opened" in event:
        risk_score += 15

    if "Window Opened" in event:
        risk_score += 25

    if "Motion Detected" in event:
        risk_score += 20

    # Vacation Mode Bonus

    if vacation_mode:
        risk_score += 20

    # Maximum 100

    risk_score = min(risk_score, 100)

    # Threat Level

    if risk_score < 30:
        level = "LOW"
        st.success(f"Threat Level: {level}")

    elif risk_score < 70:
        level = "MEDIUM"
        st.warning(f"Threat Level: {level}")

    else:
        level = "HIGH"
        st.error(f"Threat Level: {level}")

    # Risk Score

    st.metric(
        "Risk Score",
        f"{risk_score}%"
    )

    # Alert Message

    if level == "HIGH":
        st.error("🚨 ALERT GENERATED")
        st.error("Possible Intrusion Detected")

    elif level == "MEDIUM":
        st.warning("⚠ Monitor Activity")

    else:
        st.success("✅ Home Appears Safe")