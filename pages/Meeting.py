import streamlit as st
import pandas as pd
import plotly.express as px
from main import get_team_collection
teamCollection = get_team_collection()
# Load the data from CSV
df = pd.read_csv('availability.csv')
with st.form(key='team_form'):
    joining_code_input = st.text_input("Enter Team code:")
    submit_btn = st.form_submit_button(label='Enter')

    if submit_btn:
        team = teamCollection.find_one({"joining_code": joining_code_input})
# print(team)
        if team:
        # Extract the hour from the 'StartTime' and 'EndTime' columns
            df['StartTime'] = pd.to_datetime(df['StartTime']).dt.hour
            df['EndTime'] = pd.to_datetime(df['EndTime']).dt.hour

            # Create a new DataFrame to hold the availability count for each hour
            availability_count = pd.DataFrame(index=range(24))
            availability_count['Count'] = 0  # Initialize the 'Count' column with zeros

            # Loop through each row in the DataFrame
            for _, row in df.iterrows():
                # Increment the count for each hour in the range
                start_hour = row['StartTime']
                end_hour = row['EndTime']
                availability_count.loc[start_hour:end_hour, 'Count'] += 1

            # Convert the index to a time slot format in 24-hour format
            availability_count.index = pd.Series(availability_count.index).apply(lambda x: f'{x:02d}:00 - {(x + 1) % 24:02d}:00')

            # Create a horizontal bar graph with Plotly
            fig = px.bar(availability_count.reset_index(), x='Count', y='index', orientation='h', labels={'index':'Hour of Day', 'Count':'Number of Available Participants'}, title='Availability Curve')

            # Display the date selector in Streamlit
            selected_date = st.date_input('Select Date')

            # Display the plot in Streamlit
            st.plotly_chart(fig)

        else:
            st.write('Invalid Team Code')

    


