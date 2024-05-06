import streamlit as st
import random
import string
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Function to generate a random joining code
def generate_joining_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
# Display the logo image
st.image('test4.jpg')

uri = "mongodb+srv://kmmahi1810:mahi150KM@cluster0.nxwyefr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
teamCollection = client['schedi']['teamCollection']

def get_team_collection():
    teamCollection = client['schedi']['teamCollection']
    return teamCollection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Text input for team name
team_name = st.text_input("Enter team name:")

# Button to create a team
if st.button("Create Team"):
    if team_name:
        joining_code = generate_joining_code()
        db = client['schedi']
        teams = db['teamCollection']
        team_data = {"team_name": team_name, "joining_code": joining_code}
        # teams.insert_one(team_data)
        teamCollection.insert_one(team_data)
        st.write(f"Team '{team_name}' created successfully!")
        st.write(f"Joining code: {joining_code}")

# Button to join a team

with st.form(key='join_team_form'):
    st.write("Join a team")
    joining_code_input = st.text_input("Enter joining code:")
    member_name = st.text_input("Enter member name:")
    member_id = st.text_input("Enter member id:")
    submit_button = st.form_submit_button(label='Join Team')

    if submit_button:
        if member_name and member_id:
            # Find the team with the joining code
            team = teamCollection.find_one({"joining_code": joining_code_input})
            if team:
                # Add the member to the team
                teamCollection.update_one({"_id": team["_id"]}, {"$push": {"members": {"id": member_id, "name": member_name, "preference": {}}}})
                st.write(f"Successfully added '{member_name}' to the team using code: {joining_code_input}")
            else:
                st.write("Invalid joining code.")