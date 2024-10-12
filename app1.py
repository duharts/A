import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json
import streamlit.components.v1 as components  # Import streamlit components to embed HTML

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

# Add Google AdSense script
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3477424685702624"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-3477424685702624"
     data-ad-slot="XXXXXXXXXX"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

# Embed the AdSense code in the app
components.html(adsense_code, height=300)  # Adjust height based on your ad dimensions

# Title and Client Information
st.title("Lexachrom Analytical Laboratory - Certificate of Analysis")
st.subheader("NYS OCM Permit #OCM-CPL-00002")

# Use tabs to organize information for better navigation
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
    "Metals", "Moisture & Filth", "Residual Solvents", "Microbial Testing", 
    "Pesticides & Mycotoxins"
])

# (Rest of the code is unchanged)
