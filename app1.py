import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import time

# Set your Amplitude API key
AMPLITUDE_API_KEY = '98b11c5f413004992c62dacea60f6170'  # Your Amplitude API key

# Function to send events to Amplitude via HTTP API
def send_amplitude_event(event_name, event_properties=None):
    url = "https://api.amplitude.com/2/httpapi"
    payload = {
        "api_key": AMPLITUDE_API_KEY,
        "events": [
            {
                "event_type": event_name,
                "user_id": "streamlit_user",  # You can use a dynamic user ID here
                "event_properties": event_properties
            }
        ]
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            st.warning(f"Error sending event to Amplitude: {response.status_code}")
    except Exception as e:
        st.warning(f"Failed to send event: {str(e)}")

# Track Page View
send_amplitude_event('Page View', {'page': 'Lexachrom Analytical Laboratory - Certificate of Analysis'})

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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
    "Metals", "Moisture & Filth", "Residual Solvents", "Microbial Testing", 
    "Pesticides & Mycotoxins"
])

# Track tab switch event
active_tab = st.experimental_get_query_params().get('tab', ['Client & Sample Info'])[0]
send_amplitude_event('Tab Switch', {'active_tab': active_tab})

# Client Information Tab
with tab1:
    st.header("Client Information")
    st.write("""
    - **Contact Person:** Alexander S. Woodmass
    - **Phone Number:** (516) 415-7535
    - **Address:** 30 S Ocean Ave, Suite 203, Freeport, NY 11520, USA
    - **Client ID:** GROWER_1
    - **Facility Name:** Johnstown
    - **Entry Date:** 01/01/2021
    - **License Number:** MM0201M
    - **Email:** vireoquality@Vireohealth.com
    - **Phone No.:** (518) 254-6700
    - **Address:** 256 County Road 117, United States
    """)

    st.header("Sample Information")
    st.write("""
    - **Sample ID:** Pool S033WF
    - **Sample Type:** Flower
    - **Batch ID:** S033WF
    - **Batch Size:** 2456.0g
    - **Product Type:** Medical
    - **Collection Date:** 06/27/2024
    """)

# Potency and Cannabinoid Analysis Tab
with tab2:
    st.header("Potency and Cannabinoid Analysis")
    potency_data = {
        "Analyte": [
            "Cannabichromene (CBC)", "Cannabidiol (CBD)", "Cannabidiolic Acid (CBDA)", 
            "Cannabidivarin (CBDV)", "Cannabigerol (CBG)", "Cannabinol (CBN)", 
            "Delta-9-Tetrahydrocannabinol (D9-THC)", "Delta-8-Tetrahydrocannabinol (D8-THC)",
            "Tetrahydrocannabinolic Acid (THCA)", "Tetrahydrocannabivarin (THCV)", 
            "Total THC", "Total CBD"
        ],
        "Percentage": [11.18, 0.76, 1.30, 12.33, 1.03, 1.14, 1.91, 14.31, 21.41, 12.15, 20.68, 1.90]
    }
    potency_df = pd.DataFrame(potency_data)

    # Interactive Line Chart for Potency Results
    st.write("### Potency Analysis Chart")
    selected_analytes = st.multiselect("Select Analytes to Display", options=potency_df['Analyte'], default=potency_df['Analyte'])
    filtered_potency_df = potency_df[potency_df['Analyte'].isin(selected_analytes)]
    
    # Track analyte selection event
    send_amplitude_event('Analyte Selection', {'selected_analytes': selected_analytes})

    fig = px.line(filtered_potency_df, x="Analyte", y="Percentage", title="Potency Analysis", markers=True)
    fig.update_layout(xaxis_title="Analyte", yaxis_title="Percentage (%)")
    st.plotly_chart(fig)

    # Table for Potency Data
    st.write("### Potency Measurement Table")
    st.table(potency_df)

    # Summary
    st.write("""
    **Summary**:
    - Potency results show the levels of cannabinoids in the sample. 
    - Higher THC levels (e.g., 20.68%) indicate stronger psychoactive effects, while CBD (1.90%) is known for non-psychoactive therapeutic benefits.
    - Other cannabinoids like CBC and CBG also contribute to the overall medical efficacy.
    """)

# You can track other similar events for remaining tabs and components.

# Footer with a link to the original report
st.write("**Analysis Date:** 07/08/2024")
st.write("**Lab:** Lexachrom Analytical Laboratory LLC, Freeport, NY")

# Link to the original report
st.markdown("""
    **[View Original Report](https://s3-us-west-2.amazonaws.com/catsy.624/CoA+S033WF+Results+v177581-compressed.pdf?_ga=2.173394211.1804007138.1727585352-666523279.1727585352)**
""")
