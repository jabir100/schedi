# import streamlit as st
# import csv
# from main import get_team_collection
# teamCollection = get_team_collection()
# memberInfo = None
# with st.form(key='team_form'):
#     joining_code_input = st.text_input("Enter Team code:")
#     member_id = st.text_input("Enter member id:")
#     submit_btn = st.form_submit_button(label='Enter')

#     if submit_btn:
#         if member_id and joining_code_input:
#             teamInfo = teamCollection.find_one({"joining_code": joining_code_input})
#             memberInfo = teamCollection.find_one({'members': {'$elemMatch': {'id': member_id}}})
# if memberInfo:
#     with st.form(key='preference_form'):
#         # Define the days of the week
#         days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#         # Define the hours of the day in the format '1 PM - 2 PM', '2 PM - 3 PM', etc.
#         hours = [f'{str(i % 12 if i % 12 != 0 else 12)} {"AM" if i < 12 else "PM"} - {str((i+1) % 12 if (i+1) % 12 != 0 else 12)} {"AM" if i+1 < 12 else "PM"}' for i in range(24)]

#         # Create a dictionary to store the preferences
#         preferences = {day: [] for day in days}
#         print('Hello')
#         # Create a form for each day
#         for day in days:
#             st.subheader(day)
#             selected_hours = st.multiselect('Select preferred time slots:', hours, key=day)
#             print("hour", selected_hours)
#             preferences[day] = selected_hours
#         print(preferences)
#         submit_pref_btn = st.form_submit_button(label='Submit Preferences')
#         print(preferences)
#         if submit_pref_btn and all(preferences.values()):
#             with open('preferences.csv', 'a', newline='') as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow(['Day', 'Hour'])
#                 for day, hours in preferences.items():
#                     for hour in hours:
#                         writer.writerow([day, hour])
            
#             st.success('Preferences saved to preferences.csv!')
# else:
#     print("none")

import streamlit as st
import csv
from main import get_team_collection

teamCollection = get_team_collection()
memberInfo = None

with st.form(key='team_form'):
    joining_code_input = st.text_input("Enter Team code:")
    member_id = st.text_input("Enter member id:")
    submit_btn = st.form_submit_button(label='Enter')

    if submit_btn:
        if member_id and joining_code_input:
            teamInfo = teamCollection.find_one({"joining_code": joining_code_input})
            memberInfo = teamCollection.find_one({'members': {'$elemMatch': {'id': member_id}}})

if memberInfo:
    pref = {}
    with st.form(key='preference_form'):
        # Define the days of the week
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Define the hours of the day in the format '1 PM - 2 PM', '2 PM - 3 PM', etc.
        hours = [f'{str(i % 12 if i % 12 != 0 else 12)} {"AM" if i < 12 else "PM"} - {str((i+1) % 12 if (i+1) % 12 != 0 else 12)} {"AM" if i+1 < 12 else "PM"}' for i in range(24)]

        # Create a dictionary to store the preferences
        if 'preferences' not in st.session_state:
            st.session_state.preferences = {day: [] for day in days}

        # Create a form for each day
        for day in days:
            st.subheader(day)
            # st.session_state.preferences[day] = st.multiselect('Select preferred time slots:', hours, st.session_state.preferences[day], key=day)
            pref[day] = st.multiselect('Select preferred time slots:', hours, key=day)

        submit_pref_btn = st.form_submit_button(label='Submit Preferences')
        
        if submit_pref_btn and all(st.session_state.preferences.values()):
            with open('preferences.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Day', 'Hour'])
                for day, hours in st.session_state.preferences.items():
                    for hour in hours:
                        writer.writerow([day, hour])

            st.success('Preferences saved to preferences.csv!')
    print(pref.values())
# else:
#     st.write("none")
