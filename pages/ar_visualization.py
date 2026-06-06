import streamlit as st

st.title("📱 AR Security Map")

st.markdown("""
### AI-Powered Home Threat Visualization

SafeNest AR visualizes security threats across the home during Vacation Mode.
""")

st.divider()

st.image(
    "images/safenest_homepage.png",
    caption="SafeNest AR Threat Map",
    use_container_width=False
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
    🟢 Living Room
    
    Status: Safe
    
    Risk: 12%
    """)

with col2:
    st.warning("""
    🟡 Window
    
    Status: Suspicious Activity
    
    Risk: 64%
    """)

with col3:
    st.error("""
    🔴 Front Door
    
    Status: High Threat
    
    Risk: 92%
    """)