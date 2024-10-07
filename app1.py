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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
    "Metals", "Moisture & Filth", "Residual Solvents", "Microbial Testing", 
    "Pesticides & Mycotoxins"
])

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
# Track tab and chart render events
    send_amplitude_event('Tab View', {'tab': 'Potency & Cannabinoid Analysis'})
    send_amplitude_event('Chart Render', {'chart': 'Potency Analysis'})
    
# Terpene Profile Tab
with tab3:
    st.header("Terpene Profile")
    terpene_data = {
        "Terpene": ["Beta-Pinene", "Alpha-Pinene", "Limonene", "Linalool", "Beta-Caryophyllene"],
        "Percentage (%)": [3.025, 2.592, 1.709, 0.49, 0.6]
    }
    terpene_df = pd.DataFrame(terpene_data)

    # Interactive Line Chart for Terpenes
    st.write("### Terpene Profile Chart")
    selected_terpenes = st.multiselect("Select Terpenes to Display", options=terpene_df['Terpene'], default=terpene_df['Terpene'])
    filtered_terpene_df = terpene_df[terpene_df['Terpene'].isin(selected_terpenes)]
    
    fig4 = px.line(filtered_terpene_df, x="Terpene", y="Percentage (%)", title="Terpene Profile", markers=True)
    fig4.update_layout(xaxis_title="Terpene", yaxis_title="Percentage (%)")
    st.plotly_chart(fig4)

    # Table for Terpene Data
    st.write("### Terpene Measurement Table")
    st.table(terpene_df)

    # Summary
    st.write("""
    **Summary**:
    - Terpenes like Beta-Pinene and Limonene contribute to the aroma, flavor, and therapeutic effects of cannabis.
    - Each terpene has unique properties; for example, Limonene is known for its citrusy smell and potential mood-enhancing effects.
    """)

# Track tab and chart renders
    send_amplitude_event('Tab View', {'tab': 'Terpene Profile'})
    send_amplitude_event('Chart Render', {'chart': 'Terpene Profile'})

# Metals Tab
with tab4:
    st.header("Metals Testing Results")

    # Metals Data
    metals_data = {
        "Metal": ["Antimony (Sb)", "Arsenic", "Cadmium", "Chromium", "Lead", "Nickel", "Mercury"],
        "Amount (ppm)": [0.0007, 0.0006, 0.0006, 1.511, 0.154, 0.086, "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    metals_df = pd.DataFrame(metals_data)

    # Interactive Line Chart for Metals Data
    st.write("### Metals Testing Results Chart")
    fig2 = px.line(metals_df, x="Metal", y="Amount (ppm)", title="Metals Testing Results", markers=True)
    fig2.update_layout(xaxis_title="Metal", yaxis_title="Amount (ppm)")
    st.plotly_chart(fig2)

    # Table for Metals Data
    st.write("### Metals Measurement Table")
    st.table(metals_df)

    # Summary
    st.write("""
    **Summary**:
    - The metals test ensures that the sample is free from harmful heavy metals like lead and mercury, all of which passed within safe limits.
    """)

 # Track tab and chart render events
    send_amplitude_event('Tab View', {'tab': 'Metals'})
    send_amplitude_event('Chart Render', {'chart': 'Metals Testing Results'})

# Moisture & Filth Testing Tab
with tab5:
    st.header("Moisture & Filth Testing")

    moisture_data = {
        "Test": ["Moisture Content", "Water Activity", "Mammalian Excreta", "Foreign Material"],
        "Value": [14.10, 0.47, "<1mg/lb", "<5% stems, <2% other FM"]
    }
    moisture_df = pd.DataFrame(moisture_data)

    # Moisture Content and Water Activity Chart
    st.write("### Moisture Content and Water Activity Chart")
    fig5 = px.line(moisture_df, x="Test", y="Value", title="Moisture Content and Water Activity", markers=True)
    st.plotly_chart(fig5)

    # Table for Moisture & Filth Data
    st.write("### Moisture & Filth Measurement Table")
    st.table(moisture_df)

    # Summary
    st.write("""
    **Summary**:
    - The moisture content is within acceptable limits (14.10%), and the water activity (0.47) is below the threshold for microbial activity.
    - No significant levels of mammalian excreta or foreign material were detected, confirming the sample's cleanliness.
    """)

# Residual Solvents Tab
with tab6:
    st.header("Residual Solvents Testing Results")

    solvents_data = {
        "Solvent": ["Acetone", "Acetonitrile", "Total Butane", "Ethanol", "Ethyl Acetate", "Diethyl Ether", "Methanol"],
        "Amount (ppm)": ["<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    solvents_df = pd.DataFrame(solvents_data)

    # Residual Solvents Chart
    st.write("### Residual Solvents Testing Results Chart")
    fig6 = px.line(solvents_df, x="Solvent", y="Amount (ppm)", title="Residual Solvents Testing Results", markers=True)
    fig6.update_layout(xaxis_title="Solvent", yaxis_title="Amount (ppm)")
    st.plotly_chart(fig6)

    # Table for Residual Solvent Data
    st.write("### Residual Solvents Measurement Table")
    st.table(solvents_df)

    # Summary
    st.write("""
    **Summary**:
    - The residual solvents test ensures that any solvents used in the extraction process are within safe limits.
    - All solvents, including acetone and ethanol, were detected below the limit of quantitation (LOQ), indicating no harmful residues.
    """)

# Microbial and Pesticide Testing Tab
with tab7:
    st.header("Microbial and Pesticide Testing Results")

    microbial_data = {
        "Analyte": ["STEC", "Salmonella", "Total Yeast and Mold Count", "Aerobic Bacteria Count"],
        "Result": ["Negative", "Negative", "Not Detected", "Not Detected"],
        "Status": ["Pass", "Pass", "Pass", "Pass"]
    }
    microbial_df = pd.DataFrame(microbial_data)

    # Microbial Testing Chart
    st.write("### Microbial Testing Results Chart")
    fig7 = px.line(microbial_df, x="Analyte", y="Result", title="Microbial Testing Results", markers=True)
    fig7.update_layout(xaxis_title="Analyte", yaxis_title="Result")
    st.plotly_chart(fig7)

    # Table for Microbial Data
    st.write("### Microbial Measurement Table")
    st.table(microbial_df)

    # Summary
    st.write("""
    **Summary**:
    - Microbial testing ensures that no harmful microorganisms such as STEC or Salmonella are present in the sample.
    """)

# Pesticides & Mycotoxins Testing Tab
with tab8:
    st.header("Pesticides & Mycotoxins Testing Results")

    pesticides_data = {
        "Analyte": ["Aflatoxin B2", "Aflatoxin B1", "Ochratoxin A", "Aflatoxin G1", "Aflatoxin G2"],
        "Amount (ppm)": ["<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    pesticides_df = pd.DataFrame(pesticides_data)

    # Pesticides & Mycotoxins Chart
    st.write("### Pesticides & Mycotoxins Testing Results Chart")
    fig8 = px.line(pesticides_df, x="Analyte", y="Amount (ppm)", title="Pesticides & Mycotoxins Testing Results", markers=True)
    fig8.update_layout(xaxis_title="Analyte", yaxis_title="Amount (ppm)")
    st.plotly_chart(fig8)

    # Table for Pesticides & Mycotoxins Data
    st.write("### Pesticides & Mycotoxins Measurement Table")
    st.table(pesticides_df)

    # Summary
    st.write("""
    **Summary**:
    - The pesticides and mycotoxins test ensures that the sample is free from harmful pesticides and toxins. 
    - All detected levels were below the limit of quantitation (LOQ), confirming the product's safety.
    """)

# Footer with a link to the original report
st.write("**Analysis Date:** 07/08/2024")
st.write("**Lab:** Lexachrom Analytical Laboratory LLC, Freeport, NY")

# Link to the original report
st.markdown("""
    **[View Original Report](https://s3-us-west-2.amazonaws.com/catsy.624/CoA+S033WF+Results+v177581-compressed.pdf?_ga=2.173394211.1804007138.1727585352-666523279.1727585352)**
""")
