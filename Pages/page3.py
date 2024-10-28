import streamlit as st
import pandas as pd

# Initialize session state to store commute data
if "commute_data" not in st.session_state:
    st.session_state.commute_data = []

# Title of the app
st.title("Commute Performance Summary")

# Sidebar for commute input
st.sidebar.header("Enter Commute Details")

# User inputs for commute details
date = st.sidebar.date_input("Date of Commute")
travel_mode = st.sidebar.selectbox("Mode of Travel", ["Car", "Bike", "Public Transit", "Walking"])
distance = st.sidebar.number_input("Distance (in miles)", min_value=0.1, step=0.1)
time_taken = st.sidebar.number_input("Time Taken (in minutes)", min_value=1.0, step=1.0)
time_saved = st.sidebar.number_input("Time Saved Compared to Average (in minutes)", min_value=0.0, step=0.1)

# Add commute data on button click
if st.sidebar.button("Add Commute"):
    avg_speed = distance / (time_taken / 60)  # miles per hour
    commute_entry = {
        "Date": date,
        "Mode of Travel": travel_mode,
        "Distance (miles)": distance,
        "Time Taken (min)": time_taken,
        "Time Saved (min)": time_saved,
        "Average Speed (mph)": avg_speed
    }
    st.session_state.commute_data.append(commute_entry)
    st.sidebar.success("Commute Added!")

# Display commute summary if data exists
if st.session_state.commute_data:
    # Convert commute data to DataFrame
    df = pd.DataFrame(st.session_state.commute_data)

    # Calculate overall stats
    total_time_saved = df["Time Saved (min)"].sum()
    avg_speed = df["Average Speed (mph)"].mean()
    preferred_mode = df["Mode of Travel"].mode()[0]  # Most frequently chosen mode of travel

    # Display stats
    st.subheader("Commute Summary")
    st.write("**Total Time Saved:** {:.1f} minutes".format(total_time_saved))
    st.write("**Average Speed Across Commutes:** {:.1f} mph".format(avg_speed))
    st.write("**Preferred Mode of Travel:**", preferred_mode)

    # Display data in table form
    st.subheader("Commute Details")
    st.dataframe(df)

    # Insights based on data
    st.subheader("Insights")
    st.write("Based on your recent commutes, you tend to save more time when using **{}**. "
             "Your average speed of {:.1f} mph reflects an optimized commute. "
             "Keep following the recommendations for further improvement!".format(preferred_mode, avg_speed))
else:
    st.write("No commute data available. Please enter commute details in the sidebar to start tracking.")
