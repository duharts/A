import streamlit as st
import pandas as pd
import plotly.express as px

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

# Create a sidebar with a list of sections for navigation
section = st.sidebar.radio(
    "Navigate to Section",
    [
        "Client & Sample Info", 
        "Potency & Cannabinoid Analysis", 
        "Terpene Profile", 
        "Metals and Mycotoxins", 
        "Moisture & Filth", 
        "Residual Solvents", 
        "Microbial Testing", 
        "Pesticide & Aspergillus Testing"
    ]
)

# Display content based on the selected section
if section == "Client & Sample Info":
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
    - **Collection Site:** Johnstown
    """)

elif section == "Potency & Cannabinoid Analysis":
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
    st.write("### Potency Analysis")
    selected_analytes = st.multiselect("Select Analytes to Display", options=potency_df['Analyte'], default=potency_df['Analyte'])
    filtered_potency_df = potency_df[potency_df['Analyte'].isin(selected_analytes)]
    
    fig = px.line(filtered_potency_df, x="Analyte", y="Percentage", title="Potency Analysis", markers=True)
    fig.update_layout(xaxis_title="Analyte", yaxis_title="Percentage (%)")
    st.plotly_chart(fig)

    # Summary of Potency Findings
    st.write("""
    **Summary**:
    - Potency results show the levels of cannabinoids in the sample. 
    - Higher THC levels (e.g., 20.68%) indicate stronger psychoactive effects, while CBD (1.90%) is known for non-psychoactive therapeutic benefits.
    - Other cannabinoids like CBC and CBG also contribute to the overall medical efficacy.
    """)

elif section == "Terpene Profile":
    st.header("Terpene Profile")
    terpene_data = {
        "Terpene": ["Beta-Pinene", "Alpha-Pinene", "Limonene", "Linalool", "Beta-Caryophyllene"],
        "Percentage (%)": [3.025, 2.592, 1.709, 0.49, 0.6]
    }
    terpene_df = pd.DataFrame(terpene_data)

    # Interactive Line Chart for Terpenes
    st.write("### Terpene Profile")
    selected_terpenes = st.multiselect("Select Terpenes to Display", options=terpene_df['Terpene'], default=terpene_df['Terpene'])
    filtered_terpene_df = terpene_df[terpene_df['Terpene'].isin(selected_terpenes)]
    
    fig4 = px.line(filtered_terpene_df, x="Terpene", y="Percentage (%)", title="Terpene Profile", markers=True)
    fig4.update_layout(xaxis_title="Terpene", yaxis_title="Percentage (%)")
    st.plotly_chart(fig4)

    # Summary of Terpene Profile Findings
    st.write("""
    **Summary**:
    - Terpenes like Beta-Pinene and Limonene contribute to the aroma, flavor, and therapeutic effects of cannabis.
    - Each terpene has unique properties; for example, Limonene is known for its citrusy smell and potential mood-enhancing effects.
    """)

elif section == "Metals and Mycotoxins":
    st.header("Metals and Mycotoxins Testing Results")

    # Metals Data
    metals_data = {
        "Metal": ["Antimony (Sb)", "Arsenic", "Cadmium", "Chromium", "Lead", "Nickel", "Mercury"],
        "Amount (ppm)": [0.0007, 0.0006, 0.0006, 1.511, 0.154, 0.086, "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    metals_df = pd.DataFrame(metals_data)
    metals_df['Amount (ppm)'] = metals_df['Amount (ppm)'].replace('<LOQ', 0).astype(float)

    # Mycotoxins Data
    mycotoxins_data = {
        "Analyte": ["Aflatoxin B2", "Aflatoxin B1", "Ochratoxin A", "Aflatoxin G1", "Aflatoxin G2"],
        "LOQ (ppm)": [0.00141, 0.00099, 0.00113, 0.00129, 0.00114],
        "Amount (ppm)": ["<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    mycotoxins_df = pd.DataFrame(mycotoxins_data)
    mycotoxins_df['LOQ (ppm)'] = mycotoxins_df['LOQ (ppm)'].astype(float)

    # Line Chart for Metals
    st.write("### Metals Testing Results")
    fig2 = px.line(metals_df, x="Metal", y="Amount (ppm)", title="Metals Testing Results", markers=True)
    fig2.update_layout(xaxis_title="Metal", yaxis_title="Amount (ppm)")
    st.plotly_chart(fig2)

    # Line Chart for Mycotoxins
    st.write("### Mycotoxins Testing Results")
    fig3 = px.line(mycotoxins_df, x="Analyte", y="LOQ (ppm)", title="Mycotoxins Testing Results", markers=True)
    fig3.update_layout(xaxis_title="Analyte", yaxis_title="LOQ (ppm)")
    st.plotly_chart(fig3)

    # Summary of Metals & Mycotoxins Findings
    st.write("""
    **Summary**:
    - The metals test ensures that the sample is free from harmful heavy metals like lead and mercury, all of which passed within safe limits.
    - Mycotoxins such as Aflatoxins are toxic compounds produced by mold. All levels are below detection limits (LOQ), confirming the sample's safety.
    """)

# Continue similar sections for other categories like "Moisture & Filth", "Residual Solvents", "Microbial Testing", and "Pesticide & Aspergillus Testing"

# Footer
st.write("**Analysis Date:** 07/08/2024")
st.write("**Lab:** Lexachrom Analytical Laboratory LLC, Freeport, NY")
