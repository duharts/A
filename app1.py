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

# Option to toggle between one-page view and tabbed view
view_option = st.checkbox("View entire report on one page")

if view_option:
    # Single Page View
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

    # Potency Analysis Chart
    st.write("### Potency Analysis Chart")
    fig = px.line(potency_df, x="Analyte", y="Percentage", title="Potency Analysis", markers=True)
    st.plotly_chart(fig)

    # Terpene Profile
    st.header("Terpene Profile")
    terpene_data = {
        "Terpene": ["Beta-Pinene", "Alpha-Pinene", "Limonene", "Linalool", "Beta-Caryophyllene"],
        "Percentage (%)": [3.025, 2.592, 1.709, 0.49, 0.6]
    }
    terpene_df = pd.DataFrame(terpene_data)

    # Terpene Profile Chart
    st.write("### Terpene Profile Chart")
    fig4 = px.line(terpene_df, x="Terpene", y="Percentage (%)", title="Terpene Profile", markers=True)
    st.plotly_chart(fig4)

    # Metals and Mycotoxins
    st.header("Metals and Mycotoxins Testing Results")
    metals_data = {
        "Metal": ["Antimony (Sb)", "Arsenic", "Cadmium", "Chromium", "Lead", "Nickel", "Mercury"],
        "Amount (ppm)": [0.0007, 0.0006, 0.0006, 1.511, 0.154, 0.086, "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    metals_df = pd.DataFrame(metals_data)

    st.write("### Metals Testing Results Chart")
    fig2 = px.line(metals_df, x="Metal", y="Amount (ppm)", title="Metals Testing Results", markers=True)
    st.plotly_chart(fig2)

    # Residual Solvents
    st.header("Residual Solvents Testing Results")
    solvents_data = {
        "Solvent": ["Acetone", "Acetonitrile", "Total Butane", "Ethanol", "Ethyl Acetate", "Diethyl Ether", "Methanol"],
        "Amount (ppm)": ["<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ", "<LOQ"],
        "Status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }
    solvents_df = pd.DataFrame(solvents_data)

    st.write("### Residual Solvents Testing Results Chart")
    fig6 = px.line(solvents_df, x="Solvent", y="Amount (ppm)", title="Residual Solvents Testing Results", markers=True)
    st.plotly_chart(fig6)

else:
    # Tabbed View
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
        "Metals and Mycotoxins", "Moisture & Filth", "Residual Solvents", "Microbial Testing", 
        "Pesticide & Aspergillus Testing"
    ])

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

        st.write("### Potency Analysis Chart")
        fig = px.line(potency_df, x="Analyte", y="Percentage", title="Potency Analysis", markers=True)
        st.plotly_chart(fig)

    # Continue for all other tabs as in the original code...

# Footer with a link to the original report
st.write("**Analysis Date:** 07/08/2024")
st.write("**Lab:** Lexachrom Analytical Laboratory LLC, Freeport, NY")

st.markdown("""
    **[View Original Report](https://s3-us-west-2.amazonaws.com/catsy.624/CoA+S033WF+Results+v177581-compressed.pdf?_ga=2.173394211.1804007138.1727585352-666523279.1727585352)**
""")
