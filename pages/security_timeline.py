import streamlit as st

st.title("📜 Security Timeline")

events = [
    ("02:10 AM", "Motion Detected"),
    ("02:12 AM", "Unknown Person Detected"),
    ("02:13 AM", "Front Door Activity"),
    ("02:14 AM", "Threat Score Generated"),
    ("02:15 AM", "Emergency Alert Sent")
]

for time, event in events:
    st.info(f"{time} — {event}")