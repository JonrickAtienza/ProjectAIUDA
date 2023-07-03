import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
import csv
import seaborn as sns
import numpy as np
import plotly.graph_objects as go

def load_data():
    # Load the data
    data = pd.read_csv(
        "micro_world.csv",
        encoding='ISO-8859-1'
    )
    return data


def page1():
    # Write the title and the subheader
    st.title(
        "Project A.I.UDA"
    )
    st.subheader(
        """
        Assistance for Inclusion: Utilizing Data Analytics 
        """
    )

    # Load photo
    st.image("streamlit-photo-1.jpeg")

    # Load data
    data = load_data()

    # Display data
    st.markdown(
    """
    ### Group 6 Hexagonals
    - Jamie Cuadra
    - Gelo Salvador
    - Patrick Atienza
    - Mentor: Andrew Justin Oconer
    """
    )
    
    
    # st.dataframe(data)
    # st.markdown("Source: Global Findex 2021 from World Bank.")


def page2():
    # Write the title
    st.title(
        "DOLE Bayanihan Act"
    )

    st.markdown(
        """## 3.4M workers get almost P30-B cash aid via Bayanihan laws
        """
    )
    
    st.markdown(
        """
        ### _DOLE 2021_
        """
    )

        
    
#     # Load data
#     data = load_data()

#     # Fetch Philippine data
#     philippine_data = data[
#         data['economy'] == 'Philippines'
#         ]

#     # Create another column for debit card ownership
#     philippine_data['has_debit_card'] = philippine_data['fin2'].apply(
#         lambda x: 1 if x == 1 else 0
#     )

#     # Compute overall debit card ownership
#     percent_debit_card_ownership = philippine_data['has_debit_card'].sum() * 100.0 / philippine_data[
#         'wpid_random'].count()

#    # Partition the page into 2
#     col1, col2 = st.columns(2)

    # # Display text in column 1
    # col1.markdown(
    #     "In the Philippines, there is still an opportunity to expand access to financial services: "
    # )

#     # Display metric in column 2
#     col2.metric(
#         label='% of Population with Debit Card',
#         value=percent_debit_card_ownership
#     )

#     # Display text
#     st.markdown("In terms of gender breakdown:")

#     # Create another column for gender
#     philippine_data['gender'] = philippine_data['female'].apply(
#         lambda x: 'female' if x == 1 else 'male'
#     )

#     # Compute breakdown of access to debit card by gender
#     debit_by_gender = philippine_data.groupby('gender').agg(
#         total_debit_card_owners=('has_debit_card', 'sum'),
#         total_population=('wpid_random', 'count')
#     ).reset_index()

#     # Compute % debit card ownership
#     debit_by_gender['% debit card ownership'] = debit_by_gender['total_debit_card_owners'] * 100.0 / debit_by_gender[
#         'total_population']

#     # Plot the data
#     fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
#     ax.bar(
#         debit_by_gender["gender"],
#         debit_by_gender["% debit card ownership"],
#     )
#     ax.set_xlabel("Gender")
#     ax.set_ylabel("% Debit Card Ownership")

#     # Show the data
#     st.pyplot(fig)


def page3():
    # Write the title and the subheader
    st.title(
        "Bayanihan Laws"
    )
    
    st.markdown(
        """
        ### Bayanihan to Heal as One Act (2020)
        ###### _Funding: ~PHP 275 Billion_
        - ##### Main Beneficiaries: Low-income households, health workers, and affected businesses

        ### Bayanihan to Recover as One Act  (2020)
        ###### _Funding: ~PHP 214.12 Billion_
        - ##### Main Beneficiaries: Small and medium-sized enterprises (SMEs), transportation, agriculture, education, health, and social protection sectors.

        ### Bayanihan to Arise as One Act  (2021)
        ###### _Funding: ~PHP 401 Billion_
        - ##### Main Beneficiaries: Industries affected by the pandemic, individuals and households affected by the pandemic, healthcare workers, and the general public.
        """
        )
    
#     st.markdown(
#         "**Here is a bubble map presenting the % of debit card ownership per country:**"
#     )

#     # Load data
#     data = load_data()

#     # Create another column for debit card ownership
#     data['has_debit_card'] = data['fin2'].apply(
#         lambda x: 1 if x == 1 else 0
#     )

#     # Group the data and apply aggregations
#     grouped_data = data.groupby(['economy', 'economycode', 'regionwb']).agg(
#         total_debit_card_owners=('has_debit_card', 'sum'),
#         total_population=('wpid_random', 'count')
#     ).reset_index()

#     # Compute debit card ownership in %
#     grouped_data['% of population with debit card'] = grouped_data['total_debit_card_owners'] * 100.0 / grouped_data[
#         'total_population']

#     # Build the bubble map
#     fig = px.scatter_geo(
#         grouped_data,
#         locations="economycode",
#         color="regionwb",
#         hover_name="economy",
#         size="% of population with debit card",
#         projection="natural earth"
#     )

#     # Show the figure
#     st.plotly_chart(fig)


def page4():
    # Write the title
    st.title(
        "Objectives"
    )

    st.markdown(
        """ ## To investigate government reach in terms of providing aid to the low income households (second and poorest 20%) which comprise 29.2% of the Filipinos
        """
    )

def page5():
    # Write the title
    st.title(
        "Received Government Help?"
    )
    
# Partition the page into 2
    col1, col2 = st.columns(2)

    with col1:(
        """
        #### 6 out of 10 Filipinos from low income households do not receive financial aid from the government
        """
    )

    with col2:
         st.image("Low Income.png")

        
      
def page6():
    # Write the title and the subheader
    st.title(
        "Low Income, High Need"
    )
   
    col1, col2 = st.columns(2)

    with col1:(
        """
        #### - More than half of both employed and unemployed Filipinos borrowed from last year
        #### - On the average, 70.6% of those who borrowed did so for medical purposes
        """
    )
    
    with col2:
         st.image("Borrowed.png")

            
def page7():
    # Write the title and the subheader
    st.title(
        "Assistance Based on Income"
    )
   
    col1, col2 = st.columns(2)

    with col1:(
        """
        #### - Those who belong in the lower income groups are more likely are more likely to receive help from the government compared to those with higher income.
        """
    )
    
    with col2:
         st.image("Line 1.png")

def page8():
    # Write the title and the subheader
    st.title(
        "Assistance Based on Income cont."
    )
   
    col1, col2 = st.columns(2)

    with col1:(
        """
        #### - While lower income groups in the Philippines are more likely to receive government assistance, the overall proportion of the population receiving aid remains low overall
        """
    )
    
    with col2:
         st.image("Line 2.png")            
            
def page9():
    # Write the title and the subheader
    st.title(
        "Assistance Based on Income 2017 vs 2021."
    )
   
    col1, col2 = st.columns(2)

    with col1:(
        """
        #### - Government assistance has improved in all income groups from 2017 to 2021.
        #### - However, government reach to the lowest income group only slightly improved from 34.9% to 35.7%.
        """
    )
    
    with col2:
         st.image("Line 3.png")                 
            
            
def page10():
    # Write the title and the subheader
    st.title(
        "Summary"
    )
               
    st.markdown(
        """
        #### - Those belonging in low income groups receive the highest government support however, government support barely improved from 2017 to 2021  and only averages at 35.3%
        #### - More than half of those belonging in low-income groups and not receiving government support borrowed money and mostly for medical bills - citing insufficient funds
        """
    )
        
def page11():
    # Write the title and the subheader
    st.title(
        "Recommendations"
    )
 
    st.subheader(
        """
        Launch awareness and accessibility programs to People
        """
    )

    col1, col2 = st.columns(2)

    
    with col1:
         st.image("Recommendations 1.png")    
            
    with col2:(
        """
        ##### Awareness: Launch an information campaign to educate the public, especially the vulnerable sector, about the available financial assistance programs
        - ##### Ensure BSP Financial Literacy programs are implemented by LGUs
        - ##### Leverage online platforms and personalities (e.g., TikTok)
        ##### Accessibility: Launch Financial Inclusion assistance programs via digital and offline platforms
        - ##### Use of Sari-Sari stores aside from CVS to facilitate financial services (Maya Digi-Palenke)
        - ##### Mobile financial app integration (e.g., GCash, Maya)
        """
    )
    
def page12():
    # Write the title and the subheader
    st.title(
        "Recommendations"
    )
 
    st.subheader(
        """
        Assess Government reach and effectiveness
        """
    )

    col1, col2 = st.columns(2)

    with col1:(
        """
        ##### Reach: Assess who was given assistance and identify who have not benefited
        - ##### Note that only 33.8% of the Filipino population were given assistance
        ##### Effectiveness: Assess the demography with the highest need to focus on
        - ##### Income Bracket, Employment Status, Educational Background
        """
    )   
            
    with col2:
         st.image("Recommendations 2.png")    
            

        
        
list_of_pages = [
    "Project A.I.UDA",
    "DOLE Bayanihan Act",
    "Bayanihan Laws",
    "Objectives",
    "Received Government Help?",
    "Low Income, High Need",
    "Assistance Based on Income",
    "Assistance Based on Income cont.",
    "Assistance Based on Income 2017 vs 2021.",
    "Summary",
    "Recommendations 1",
    "Recommendations 2"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Project A.I.UDA":
    page1()

elif selection == "DOLE Bayanihan Act":
    page2()

elif selection == "Bayanihan Laws":
    page3()

elif selection == "Objectives":
    page4()

elif selection == "Received Government Help?":
    page5()
    
elif selection == "Low Income, High Need":
    page6()

elif selection == "Assistance Based on Income":
    page7()
    
elif selection == "Assistance Based on Income cont.":
    page8()
    
elif selection == "Assistance Based on Income 2017 vs 2021.":
    page9()
    
elif selection == "Summary":
    page10()     
        
elif selection == "Recommendations 1":
    page11()        
    
elif selection == "Recommendations 2":
    page12()