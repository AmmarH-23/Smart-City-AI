import openai
import streamlit as st
import os

# Set up OpenAI API key
openai.api_key = os.getenv("INSERT-YOUR-API-KEY")

# Function to generate traffic alert notifications
def generate_traffic_alert(traffic_data, weather_data):
    prompt = f"Current traffic conditions: {traffic_data}\nCurrent weather conditions: {weather_data}\n\nGenerate an alert to help users plan their commute more efficiently."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message['content'].strip()

# Streamlit UI setup
st.title("Traffic Alert Notifications")

# User selection for weather conditions
weather_data = st.selectbox(
    "Select the current weather conditions:",
    ("Clear skies, mild temperature", "Cloudy skies, cold temperature", "Heavy rain", "Snowy")
)

# User selection for traffic conditions
traffic_data = st.selectbox(
    "Select the current traffic conditions:",
    ("Low traffic", "Moderate traffic", "High traffic", "Heavy congestion")
)

# Button to generate traffic alert
if st.button("Get Traffic Alert"):
    alert = generate_traffic_alert(traffic_data, weather_data)
    st.write("### Traffic Alert:")
    st.write(alert)
