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

# Use tabs to organize information for better navigation
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
    "Metals and Mycotoxins", "Moisture & Filth", "Residual Solvents", "Microbial Testing", 
    "Pesticide & Aspergillus Testing"
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
    - **Collection Site:** Johnstown
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

    # Summary of Potency Findings
    st.write("""
    **Summary**:
    - Potency results show the levels of cannabinoids in the sample. 
    - Higher THC levels (e.g., 20.68%) indicate stronger psychoactive effects, while CBD (1.90%) is known for non-psychoactive therapeutic benefits.
    - Other cannabinoids like CBC and CBG also contribute to the overall medical efficacy.
    """)

    # Table for Potency Data
    st.write("### Potency Measurement Table")
    st.table(potency_df)

    # Interactive Line Chart for Potency Results
    st.write("### Potency Analysis Chart")
    selected_analytes = st.multiselect("Select Analytes to Display", options=potency_df['Analyte'], default=potency_df['Analyte'])
    filtered_potency_df = potency_df[potency_df['Analyte'].isin(selected_analytes)]
    
    fig = px.line(filtered_potency_df, x="Analyte", y="Percentage", title="Potency Analysis", markers=True)
    fig.update_layout(xaxis_title="Analyte", yaxis_title="Percentage (%)")
    st.plotly_chart(fig)

# Terpene Profile Tab
with tab3:
    st.header("Terpene Profile")
    terpene_data = {
        "Terpene": ["Beta-Pinene", "Alpha-Pinene", "Limonene", "Linalool", "Beta-Caryophyllene"],
        "Percentage (%)": [3.025, 2.592, 1.709, 0.49, 0.6]
    }
    terpene_df = pd.DataFrame(terpene_data)

    # Summary of Terpene Profile Findings
    st.write("""
    **Summary**:
    - Terpenes like Beta-Pinene and Limonene contribute to the aroma, flavor, and therapeutic effects of cannabis.
    - Each terpene has unique properties; for example, Limonene is known for its citrusy smell and potential mood-enhancing effects.
    """)

    # Table for Terpene Data
    st.write("### Terpene Measurement Table")
    st.table(terpene_df)

    # Interactive Line Chart for Terpenes
    st.write("### Terpene Profile Chart")
    selected_terpenes = st.multiselect("Select Terpenes to Display", options=terpene_df['Terpene'], default=terpene_df['Terpene'])
    filtered_terpene_df = terpene_df[terpene_df['Terpene'].isin(selected_terpenes)]
    
    fig4 = px.line(filtered_terpene_df, x="Terpene", y="Percentage (%)", title="Terpene Profile", markers=True)
    fig4.update_layout(xaxis_title="Terpene", yaxis_title="Percentage (%)")
    st.plotly_chart(fig4)

# Metals and Mycotoxins Tab
with tab4:
    st.header("Metals and Mycotoxins Testing Results")

    # Metals Data
    metals_data = {
        "Metal": ["Antimony (Sb)", "Arsenic", "Cadmium", "Chromium", "Lead", "Nickel", "Mercury"],
        "Amount (ppm)": [0.0007, 0.0006, 0.0006, 1.511, 0.154, 0.086, "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    metals_df = pd.DataFrame(metals_data)

    # Summary of Metals & Mycotoxins Findings
    st.write("""
    **Summary**:
    - The metals test ensures that the sample is free from harmful heavy metals like lead and mercury, all of which passed within safe limits.
    """)

    # Table for Metals Data
    st.write("### Metals Measurement Table")
    st.table(metals_df)

    # Interactive Line Chart for Metals Data
    st.write("### Metals Testing Results Chart")
    fig2 = px.line(metals_df, x="Metal", y="Amount (ppm)", title="Metals Testing Results", markers=True)
    fig2.update_layout(xaxis_title="Metal", yaxis_title="Amount (ppm)")
    st.plotly_chart(fig2)

    # Mycotoxins Data
    mycotoxins_data = {
        "Analyte": ["Aflatoxin B2", "Aflatoxin B1", "Ochratoxin A", "Aflatoxin G1", "Aflatoxin G2"],
        "LOQ (ppm)": [0.00141, 0.00099, 0.00113, 0.00129, 0.00114],
        "Amount (ppm)": ["<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    mycotoxins_df = pd.DataFrame(mycotoxins_data)

    # Table for Mycotoxins Data
    st.write("### Mycotoxins Measurement Table")
    st.table(mycotoxins_df)

    # Interactive Line Chart for Mycotoxins Data
    st.write("### Mycotoxins Testing Results Chart")
    fig3 = px.line(mycotoxins_df, x="Analyte", y="LOQ (ppm)", title="Mycotoxins Testing Results", markers=True)
    fig3.update_layout(xaxis_title="Analyte", yaxis_title="LOQ (ppm)")
    st.plotly_chart(fig3)

# Moisture Content & Filth Testing Tab
with tab5:
    st.header("Moisture Content and Filth Testing")

    # Data for moisture content and filth testing
    moisture_data = {
        "Test": ["Moisture Content", "Water Activity", "Mammalian Excreta", "Foreign Material"],
        "Value": [14.10, 0.47, "< 1mg/lb", "< 5% stems, < 2% other FM"]
    }
    moisture_df = pd.DataFrame(moisture_data)

    # Summary of Moisture & Filth Findings
    st.write("""
    **Summary**:
    - Moisture content and water activity are key indicators of product freshness and susceptibility to microbial growth.
    - The moisture content is within acceptable limits (14.10%), and the water activity (0.47) is below the threshold for microbial activity, ensuring product stability.
    - No significant levels of mammalian excreta or foreign material were detected, confirming the sample's cleanliness.
    """)

    # Table for Moisture and Filth Data
    st.write("### Moisture & Filth Measurement Table")
    st.table(moisture_df)

    # Interactive Line Chart for Moisture Content and Water Activity
    st.write("### Moisture Content and Water Activity Chart")
    fig5 = px.line(moisture_df, x="Test", y="Value", title="Moisture Content and Water Activity", markers=True)
    fig5.update_layout(xaxis_title="Test", yaxis_title="Value")
    st.plotly_chart(fig5)

# Residual Solvents Tab
with tab6:
    st.header("Residual Solvents Testing Results")

    solvents_data = {
        "Solvent": ["Acetone", "Acetonitrile", "Total Butane", "Ethanol", "Ethyl Acetate", "Diethyl Ether", "Methanol"],
        "Amount (ppm)": ["<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    solvents_df = pd.DataFrame(solvents_data)

    # Summary of Residual Solvents Findings
    st.write("""
    **Summary**:
    - The residual solvents test ensures that any solvents used in the extraction process are within safe limits.
    - All solvents, including acetone and ethanol, were detected below the limit of quantitation (LOQ), indicating no harmful residues.
    """)

    # Table for Residual Solvent Data
    st.write("### Residual Solvents Measurement Table")
    st.table(solvents_df)

    # Interactive Line Chart for Residual Solvents Data
    st.write("### Residual Solvents Testing Results Chart")
    fig6 = px.line(solvents_df, x="Solvent", y="Amount (ppm)", title="Residual Solvents Testing Results", markers=True)
    fig6.update_layout(xaxis_title="Solvent", yaxis_title="Amount (ppm)")
    st.plotly_chart(fig6)

# Microbial and Pesticides Testing Tab
with tab7:
    st.header("Microbial and Pesticides Testing Results")

    # Microbial Data
    microbial_data = {
        "Analyte": ["STEC", "Salmonella", "Total Yeast and Mold Count", "Aerobic Bacteria Count"],
        "Result": ["Negative", "Negative", "Not Detected", "Not Detected"],
        "Status": ["Pass", "Pass", "Pass", "Pass"]
    }
    microbial_df = pd.DataFrame(microbial_data)

    # Summary of Microbial Findings
    st.write("""
    **Summary**:
    - Microbial testing ensures that no harmful microorganisms such as STEC or Salmonella are present in the sample.
    """)

    # Table for Microbial Data
    st.write("### Microbial Measurement Table")
    st.table(microbial_df)

    # Interactive Line Chart for Microbial Data
    st.write("### Microbial Testing Results Chart")
    fig7 = px.line(microbial_df, x="Analyte", y="Result", title="Microbial Testing Results", markers=True)
    fig7.update_layout(xaxis_title="Microbial Analyte", yaxis_title="Result")
    st.plotly_chart(fig7)

# Aspergillus Testing Tab
with tab8:
    st.header("Aspergillus Testing Results")

    aspergillus_data = {
        "Analyte": ["Aspergillus Flavus", "Aspergillus Fumigatus", "Aspergillus Niger", "Aspergillus Terreus"],
        "Result": ["Negative", "Negative", "Negative", "Negative"],
        "Status": ["Pass", "Pass", "Pass", "Pass"]
    }
    aspergillus_df = pd.DataFrame(aspergillus_data)

    # Summary of Aspergillus Findings
    st.write("""
    **Summary**:
    - Aspergillus is a genus of mold that can be harmful if present in cannabis products.
    - The sample tested negative for all species of Aspergillus (Flavus, Fumigatus, Niger, Terreus), ensuring product safety.
    """)

    # Table for Aspergillus Data
    st.write("### Aspergillus Measurement Table")
    st.table(aspergillus_df)

    # Interactive Line Chart for Aspergillus Testing Results
    st.write("### Aspergillus Testing Results Chart")
    fig9 = px.line(aspergillus_df, x="Analyte", y="Result", title="Aspergillus Testing Results", markers=True)
    fig9.update_layout(xaxis_title="Aspergillus Analyte", yaxis_title="Result")
    st.plotly_chart(fig9)

# Footer
st.write("**Analysis Date:** 07/08/2024")
st.write("**Lab:** Lexachrom Analytical Laboratory LLC, Freeport, NY")
