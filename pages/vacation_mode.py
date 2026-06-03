import streamlit as st
import json
import os

# FILE = "data/vacation_mode.json"

# if not os.path.exists(FILE):
#     with open(FILE, "w") as f:
#         json.dump({"vacation_mode": False}, f)

# with open(FILE, "r") as f:
#     data = json.load(f)

# st.title("✈ Vacation Mode")

# vacation_mode = st.toggle(
#     "Enable Vacation Mode",
#     value=data["vacation_mode"]
# )

# if st.button("Save Status"):

#     with open(FILE, "w") as f:
#         json.dump(
#             {"vacation_mode": vacation_mode},
#             f
#         )

#     st.success("Status Updated")

st.title("✈ Vacation Mode")
vacation_mode=st.toggle(
    "Enable Vacation Mode"
)
if vacation_mode:

    st.success("""
    🟢 Vacation Mode Active
    
    Enhanced Security Monitoring Enabled
    """)

else:

    st.info("""
    🔵 Vacation Mode Disabled
    
    Normal Monitoring Active
    """)
if vacation_mode:

    # st.warning("""
    # Security Rules Activated
    
    # ✓ Monitor Door Activity
    # ✓ Monitor Window Activity
    # ✓ Monitor Motion Events
    # ✓ Increase Threat Sensitivity
    # ✓ Generate Alerts
    # """)
    col1, col2, col3 = st.columns(3)

    col1.metric(
    "Security Status",
    "ACTIVE"
    )

    col2.metric(
    "Monitoring",
    "24/7"
    )

    col3.metric(
    "Risk Level",
    "HIGH ALERT"
    )