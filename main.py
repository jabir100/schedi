import streamlit as st
import random
import string

# Function to generate a random joining code
def generate_joining_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Display the logo image
st.image('test4.jpg')

# Add some space
st.write("\n\n")


# Button to create a team
if st.button("Create Team"):
    team_name = st.text_input("Enter team name:")
    if team_name:
        joining_code = generate_joining_code()
        # Store the team name and joining code in the database
        # Here you would typically use your database integration, such as SQLite or MongoDB
        # For simplicity, we'll just print the message
        st.write(f"Team '{team_name}' created successfully!")
        st.write(f"Joining code: {joining_code}")

# Button to join a team
if st.button("Join Team"):
    joining_code_input = st.text_input("Enter joining code:")
    if joining_code_input:
        # Check if the joining code exists in the database
        # Here you would typically query your database to verify the joining code
        # For simplicity, we'll just print a message
        st.write(f"Successfully joined the team using code: {joining_code_input}")
