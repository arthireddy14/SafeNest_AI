import streamlit as st
import json
import os
import joblib
import pandas as pd

model = joblib.load("threat_model.pkl")

person_encoder = joblib.load(
    "person_encoder.pkl"
)

time_encoder = joblib.load(
    "time_encoder.pkl"
)

threat_encoder = joblib.load(
    "threat_encoder.pkl"
)

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

previous_incidents = st.slider(
    "Previous Security Incidents",
    0,
    5,
    0
)

# -----------------------------
# Analyze Button
# -----------------------------

if st.button("Analyze Threat"):

    motion = int(
        "Motion Detected" in event
    )

    door = int(
        "Door Opened" in event
    )

    window = int(
        "Window Opened" in event
    )

    vacation = int(vacation_mode)

    encoded_person = person_encoder.transform(
        [
            person.replace(
                " Person",
                ""
            )
        ]
    )[0]

    encoded_time = time_encoder.transform(
        [time_of_day]
    )[0]

    input_data = pd.DataFrame(
        [[
            encoded_person,
            encoded_time,
            motion,
            door,
            window,
            vacation,
            previous_incidents
        ]],
        columns=[
            "person",
            "time",
            "motion",
            "door",
            "window",
            "vacation",
            "previous_incidents"
        ]
    )

    prediction = model.predict(
        input_data
    )[0]

    STATS_FILE = "data/stats.json"

    if os.path.exists(STATS_FILE):

        with open(STATS_FILE, "r") as f:
            stats = json.load(f)

    else:

        stats = {
        "threats_analyzed": 0
        }

    stats["threats_analyzed"] += 1

    with open(STATS_FILE, "w") as f:
        json.dump(
        stats,
        f,
        indent=4
        )
    
    threat_level = (
        threat_encoder
        .inverse_transform(
            [prediction]
        )[0]
    )

    probabilities = model.predict_proba(
        input_data
    )[0]

    risk_score = round(
        max(probabilities) * 100,
        2
    )
    if threat_level == "High":

        st.error(
        f"🚨 Threat Level: {threat_level}"
        )

    elif threat_level == "Medium":

        st.warning(
        f"⚠ Threat Level: {threat_level}"
        )

    else:

        st.success(
        f"✅ Threat Level: {threat_level}"
        )
    
    st.metric(
    "Risk Score",
    f"{risk_score}%"
    )

    st.subheader(
    "🛡 Safety Recommendations"
    )

    if threat_level == "High":

        st.error("""
    • Notify Homeowner

    • Verify CCTV Feed

    • Activate Alarm

    • Contact Security Services
    """)

    elif threat_level == "Medium":

        st.warning("""
    • Monitor Activity

    • Check Entry Points

    • Verify Visitor Identity
    """)

    else:

        st.success("""
    • Home Appears Secure

    • Continue Monitoring
    """)