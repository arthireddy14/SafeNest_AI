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
    
    if not name.strip():
        st.error("Please enter a name")
        st.stop()

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

    for index, member in enumerate(members):

        st.info(
        f"""
        👤 {member['name']}

        Relationship: {member['relationship']}

        Age: {member['age']}
        """
        )

        
            
st.divider()

st.subheader("📋 Registered Family Members")

with open(FILE_PATH, "r") as f:
    members = json.load(f)

if members:

    for index, member in enumerate(members):

        st.info(
            f"""
            👤 {member['name']}

            Relationship: {member['relationship']}

            Age: {member['age']}
            """
        )

        if st.button(
            f"❌ Delete {member['name']}",
            key=f"delete_{index}"
        ):

            members.pop(index)

            with open(FILE_PATH, "w") as f:
                json.dump(
                    members,
                    f,
                    indent=4
                )

            st.success("Member Deleted")
            st.rerun()

else:
    st.warning("No members registered yet.")