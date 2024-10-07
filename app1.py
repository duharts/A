import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json

# Set your Amplitude API key
AMPLITUDE_API_KEY = '98b11c5f413004992c62dacea60f6170'  # Ensure your API key is correct

# Function to send events to Amplitude via HTTP API
def send_amplitude_event(event_name, event_properties=None):
    url = "https://api.amplitude.com/2/httpapi"
    payload = {
        "api_key": AMPLITUDE_API_KEY,
        "events": [
            {
                "event_type": event_name,
                "user_id": "streamlit_user",  # Static user ID; modify as needed
                "event_properties": event_properties
            }
        ]
    }
    
    try:
        response = requests.post(url, json=payload)
        
        # Debugging: Show status and response in Streamlit
        if response.status_code == 200:
            st.write(f"Event '{event_name}' sent successfully.")
        else:
            st.error(f"Error sending event '{event_name}'. Status: {response.status_code}. Response: {response.text}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to send event '{event_name}'. Error: {str(e)}")

# Track a page view event to verify tracking
send_amplitude_event('Page View', {'page': 'Lexachrom Analytical Laboratory'})
# Add the Lexachrom logo to the header and center it
logo_url = "https://www.lexachrom.com/images/logo_v_2.svg"
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='{logo_url}' width='200'>
    </div>
    """, 
    unsafe_allow_html=True
)

# Title and Client Information
st.title("Lexachrom Analytical Laboratory - Certificate of Analysis")
st.subheader("NYS OCM Permit #OCM-CPL-00002")

# Use tabs to organize information for better navigation
tab1, tab2 = st.tabs(["Client & Sample Info", "Potency & Cannabinoid Analysis"])

# Client Information Tab
with tab1:
    st.header("Client Information")
    st.write("""
    - **Contact Person:** Alexander S. Woodmass
    - **Phone Number:** (516) 415-7535
    - **Address:** 30 S Ocean Ave, Suite 203, Freeport, NY 11520, USA
    """)
    send_amplitude_event('Tab View', {'tab': 'Client & Sample Info'})

# Potency and Cannabinoid Analysis Tab
with tab2:
    st.header("Potency and Cannabinoid Analysis")
    potency_data = {
        "Analyte": ["THC", "CBD", "CBN", "CBG"],
        "Percentage": [20.5, 5.2, 1.3, 0.9]
    }
    potency_df = pd.DataFrame(potency_data)
    
    fig = px.line(potency_df, x="Analyte", y="Percentage", title="Potency Analysis", markers=True)
    st.plotly_chart(fig)
    
    send_amplitude_event('Tab View', {'tab': 'Potency & Cannabinoid Analysis'})
    send_amplitude_event('Chart Render', {'chart': 'Potency Analysis'})

# Track a button click event
if st.button('Download Report'):
    send_amplitude_event('Button Click', {'button': 'Download Report'})

# Footer with analysis date
st.write("**Analysis Date:** 07/08/2024")
st.write("**Lab:** Lexachrom Analytical Laboratory LLC, Freeport, NY")

# Link to the original report
st.markdown("""
    **[View Original Report](https://s3-us-west-2.amazonaws.com/catsy.624/CoA+S033WF+Results+v177581-compressed.pdf?_ga=2.173394211.1804007138.1727585352-666523279.1727585352)**
""")
