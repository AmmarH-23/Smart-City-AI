import streamlit as st
from openai import OpenAI

client = OpenAI(api_key='INSERT-API-KEY')

# Function to analyze data and recommend route
def recommend_route(origin, destination, traffic_data, transit_data, weather_data):
    # Construct the input message for OpenAI API
    prompt = f"Origin: {origin}\nDestination: {destination}\nTraffic: {traffic_data}\nTransit: {transit_data}\nWeather: {weather_data}\n\nRecommend the optimal travel route, specifying if driving, public transit, or walking is most efficient."

    try:
        # Updated API call for chat-based models like gpt-3.5-turbo
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI setup
st.title("Predictive Route Optimization")

# User input for origin and destination
origin = st.text_input("Enter your starting point (origin):")
destination = st.text_input("Enter your destination:")

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

# User selection for train schedule
transit_data = st.selectbox(
    "Select the current train schedule status:",
    ("Operating normally", "Delayed", "Not operating", "Limited service")
)

# Process recommendation if inputs are provided
if origin and destination:
    route_recommendation = recommend_route(origin, destination, traffic_data, transit_data, weather_data)
    st.write("### Recommended Route:")
    st.write(route_recommendation)
else:
    st.write("Please enter both origin and destination to get a route recommendation.")

