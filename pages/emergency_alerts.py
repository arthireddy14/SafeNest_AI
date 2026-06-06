import streamlit as st

st.title("🚨 Emergency Alerts")

alerts = [
    {
        "time":"02:14 AM",
        "event":"Unknown Person Detected",
        "severity":"HIGH"
    },
    {
        "time":"02:20 AM",
        "event":"Window Opened",
        "severity":"MEDIUM"
    }
]

for alert in alerts:

    st.error(
        f"""
        Time: {alert['time']}

        Event: {alert['event']}

        Severity: {alert['severity']}
        """
    )