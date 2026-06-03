import streamlit as st
import json
import os

FILE_PATH = "data/family.json"

# Create file if not exists
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        json.dump([], f)

st.title("👨‍👩‍👧 Family Registry")

st.subheader("Register Authorized Family Members")

name = st.text_input("Full Name")

relationship = st.selectbox(
    "Relationship",
    [
        "Owner",
        "Father",
        "Mother",
        "Brother",
        "Sister",
        "Grandfather",
        "Grandmother",
        "Other"
    ]
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120
)

if st.button("➕ Add Member"):

    with open(FILE_PATH, "r") as f:
        members = json.load(f)

    members.append({
        "name": name,
        "relationship": relationship,
        "age": age
    })

    with open(FILE_PATH, "w") as f:
        json.dump(members, f, indent=4)

    st.success("Member Added Successfully!")
    
    
st.divider()

st.subheader("📋 Registered Family Members")

with open(FILE_PATH, "r") as f:
    members = json.load(f)

if members:

    for member in members:
        
    #      col1, col2, col3 = st.columns(3)

    # col1.metric("Name", member["name"])
    # col2.metric("Role", member["relationship"])
    # col3.metric("Age", member["age"])

    # st.divider()

        st.info(
            f"""
            👤 {member['name']}
            
            Relationship: {member['relationship']}
            
            Age: {member['age']}
            """
        )

else:
    st.warning("No members registered yet.")