
import streamlit as st
import json
import os

st.set_page_config(
    page_title="SafeNest AI",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 SafeNest AI")
st.subheader("Secure Homes. Peaceful Journeys.")

st.markdown("""
### Welcome to SafeNest AI

An AI-powered home security assistant designed to help homeowners monitor their homes while away.

### Features

✅ Family Registry

✅ Vacation Mode

✅ Threat Analysis

✅ Risk Assessment
""")

col1, col2, col3 = st.columns(3)

FILE_PATH = "data/family.json"

member_count = 0

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        members = json.load(f)
        member_count = len(members)
       
STATS_FILE = "data/stats.json"

threats_count = 0

if os.path.exists(STATS_FILE):
    with open(STATS_FILE, "r") as f:
        stats = json.load(f)
        threats_count = stats.get(
            "threats_analyzed",
            0
        )
        
              
col1.metric(
    "Registered Members",
    member_count
)


col2.metric(
    "Threats Analyzed",
    threats_count
)

col3.metric(
    "Security Status",
    "Protected"
)

st.divider()

st.subheader("🚀 System Overview")

st.info("""
SafeNest AR combines Artificial Intelligence and Augmented Reality concepts
to help families monitor home security during vacations and emergencies.
""")