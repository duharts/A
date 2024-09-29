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

# Add a summary section at the top for key metrics
st.markdown("## Key Metrics Summary")
st.markdown("""
- **Total THC:** 20.68%
- **Total CBD:** 1.90%
- **Metals:** Pass
- **Mycotoxins:** Pass
- **Microbial Testing:** Pass
- **Pesticides:** Pass
- **Aspergillus:** Pass
""")

# Provide a toggle for detailed view
detailed_view = st.checkbox("Show Detailed Analysis")

# Use fewer tabs by grouping related information
tab1, tab2, tab3 = st.tabs(["Client & Sample Info", "Quality Analysis", "Safety Testing"])

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
    - **Collection Site:** Johnstown
    """)

# Quality Analysis Tab
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
    st.write("### Potency Analysis")
    selected_analytes = st.multiselect("Select Analytes to Display", options=potency_df['Analyte'], default=potency_df['Analyte'])
    filtered_potency_df = potency_df[potency_df['Analyte'].isin(selected_analytes)]
    
    fig = px.bar(filtered_potency_df, x="Analyte", y="Percentage", title="Potency Analysis", color="Percentage", labels={'Percentage': 'Percentage (%)'})
    fig.update_layout(xaxis_title="Analyte", yaxis_title="Percentage (%)")
    st.plotly_chart(fig)

    # Summary of Potency Findings
    st.write("""
    **Summary**:
    - Higher THC levels (20.68%) suggest stronger psychoactive effects.
    - CBD (1.90%) contributes non-psychoactive therapeutic benefits.
    """)

    # Terpene Profile
    if detailed_view:
        st.header("Terpene Profile")
        terpene_data = {
            "Terpene": ["Beta-Pinene", "Alpha-Pinene", "Limonene", "Linalool", "Beta-Caryophyllene"],
            "Percentage (%)": [3.025, 2.592, 1.709, 0.49, 0.6]
        }
        terpene_df = pd.DataFrame(terpene_data)

        st.write("### Terpene Profile")
        selected_terpenes = st.multiselect("Select Terpenes to Display", options=terpene_df['Terpene'], default=terpene_df['Terpene'])
        filtered_terpene_df = terpene_df[terpene_df['Terpene'].isin(selected_terpenes)]

        fig4 = px.bar(filtered_terpene_df, x="Terpene", y="Percentage (%)", title="Terpene Profile", color="Percentage (%)")
        fig4.update_layout(xaxis_title="Terpene", yaxis_title="Percentage (%)")
        st.plotly_chart(fig4)

        st.write("""
        **Summary**:
        - Terpenes like Beta-Pinene and Limonene contribute to aroma and potential therapeutic effects.
        """)

# Safety Testing Tab
with tab3:
    st.header("Safety Testing")
    
    # Metals & Mycotoxins
    if detailed_view:
        st.subheader("Metals and Mycotoxins Testing")

        metals_data = {
            "Metal": ["Antimony (Sb)", "Arsenic", "Cadmium", "Chromium", "Lead", "Nickel", "Mercury"],
            "Amount (ppm)": [0.0007, 0.0006, 0.0006, 1.511, 0.154, 0.086, 0.0],
            "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
        }
        metals_df = pd.DataFrame(metals_data)

        st.write("### Metals Testing")
        fig2 = px.bar(metals_df, x="Metal", y="Amount (ppm)", title="Metals Testing", color="Amount (ppm)", labels={'Amount (ppm)': 'Amount (ppm)'})
        fig2.update_layout(xaxis_title="Metal", yaxis_title="Amount (ppm)")
        st.plotly_chart(fig2)

        mycotoxins_data = {
            "Analyte": ["Aflatoxin B2", "Aflatoxin B1", "Ochratoxin A", "Aflatoxin G1", "Aflatoxin G2"],
            "Amount (ppm)": [0.0, 0.0, 0.0, 0.0, 0.0],
            "Status": ["Pass", "Pass", "Pass", "Pass", "Pass"]
        }
        mycotoxins_df = pd.DataFrame(mycotoxins_data)

        st.write("### Mycotoxins Testing")
        fig3 = px.bar(mycotoxins_df, x="Analyte", y="Amount (ppm)", title="Mycotoxins Testing", color="Amount (ppm)")
        fig3.update_layout(xaxis_title="Analyte", yaxis_title="Amount (ppm)")
        st.plotly_chart(fig3)

    # Microbial & Pesticides
    st.subheader("Microbial and Pesticide Testing")
    
    microbial_data = {
        "Analyte": ["STEC", "Salmonella", "Total Yeast and Mold Count", "Aerobic Bacteria Count"],
        "Result": ["Negative", "Negative", "Not Detected", "Not Detected"],
        "Status": ["Pass", "Pass", "Pass", "Pass"]
    }
    microbial_df = pd.DataFrame(microbial_data)

    st.write("### Microbial Testing Results")
    fig7 = px.bar(microbial_df, x="Analyte", y="Result", title="Microbial Testing Results", color="Result")
    fig7.update_layout(xaxis_title="Microbial Analyte", yaxis_title="Result")
    st.plotly_chart(fig7)

    pesticide_data = {
        "Pesticide": ["Aflatoxin B2", "Aflatoxin B1", "Ochratoxin A", "Aflatoxin G1", "Aflatoxin G2"],
        "Amount (ppm)": [0.0, 0.0, 0.0, 0.0, 0.0],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    pesticide_df = pd.DataFrame(pesticide_data)

    st.write("### Pesticide Testing Results")
    fig8 = px.bar(pesticide_df, x="Pesticide", y="Amount (ppm)", title="Pesticide Testing Results", color="Amount (ppm)")
    fig8.update_layout(xaxis_title="Pesticide", yaxis_title="Amount (ppm)")
    st.plotly_chart(fig8)

# Footer with consistent information
st.write("""
---
**Analysis Date:** 07/08/2024  
**Lab:** Lexachrom Analytical Laboratory LLC, Freeport, NY
""")

# Optional export to PDF button for generating reports
st.download_button(label="Download Report as PDF", data="report.pdf", file_name="Lexachrom_Certificate_of_Analysis.pdf")
