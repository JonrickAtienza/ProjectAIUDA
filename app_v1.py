import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
import os


# Change default working directory
#os.chdir(r"C:\Users\Jamie\esk\esk_sprint1\dsf11-sprint-1-main\streamlit_files")
#os.getcwd()

# Function for loading the data
def load_data():
    # Load the data
    data = pd.read_csv(
        r"micro_world.csv",
        encoding='ISO-8859-1'
    )
    return data

def load_data17():
    # Load the data
    data = pd.read_csv(
        r"micro_world_2017.csv",
        encoding='ISO-8859-1'
    )
    return data


def introduction():    
    # Title and Subheader
    st.title("Assistance for Inclusion: Utilizing Data Analytics")    
    st.image("intro_photo_01.jpg")
    
    # Government Laws
    st.title("")
    st.subheader("DOLE 2021")
    st.write("Lorem ipsum")
    st.image("intro_photo_02.jpg")
    
    st.title("")
    st.subheader("Bayanihan Laws")
    st.write("Lorem ipsum")
    st.image("intro_photo_03.jpg")

    
def objective():
    st.title("Objective:")
    st.subheader("To investigate government reach in terms of providing aid to the low income households (second and poorest 20%) which comprise *29.2% of the Filipinos")
   
    
    st.write("*From the survey data of the [Global Findex 2021 from World Bank](https://microdata.worldbank.org/index.php/catalog/4607/data-dictionary/F1?file_name=micro_world.dta)")
    # Load data
    data = load_data()

    # Display data
    st.markdown("**The Data**")
    st.dataframe(data)


def govt_help_stats():
    st.write('**<p style="font-size:32px; color:#007C80;">Government Reach: At a Glance</p>**', unsafe_allow_html=True)    
    col1, col2 = st.columns(2)

    with col1:(
        """
        #### 6 out of 10 Filipinos from low income households do not receive financial aid from the government
        """ )

    with col2:
         st.image("page2_01.jpg")
    
    st.title("")
    st.write('**<p style="font-size:32px; color:#007C80;">Low Income, High Need</p>**', unsafe_allow_html=True)
    st.markdown("_Among those belonging in low-income groups and did not receive financial help._")

    
def income_group():
    st.title("Government Assistance per Income Group")
    
    
    # Data Prep
    data = load_data()
    data_17 = load_data17()
    ph_data = data[data['economy'] == 'Philippines']
    ph_data['emp_in'] = ph_data['emp_in'].replace({1: 'Employed', 2: 'Unemployed'})
    ph_data['inc_q'] = ph_data['inc_q'].replace({ 1: 'poorest 20%',
                                                                   2: 'second 20%',
                                                                   3: 'middle 20%',
                                                                   4: 'fourth 20%',
                                                                   5: 'richest 20%'})
    
    ph_data_17 = data_17[data_17['economy'] == 'Philippines']
    ph_data_17['emp_in'] = ph_data_17['emp_in'].replace({1: 'Employed', 2: 'Unemployed'})
    ph_data_17['inc_q'] = ph_data_17['inc_q'].replace({ 1: 'poorest 20%',
                                                                   2: 'second 20%',
                                                                   3: 'middle 20%',
                                                                   4: 'fourth 20%',
                                                                   5: 'richest 20%'})
    
    # Filter columns
    government_help    = ph_data[['wpid_random', 'emp_in', 'inc_q', 'fin37']]
    government_help_17 = ph_data_17[['wpid_random', 'emp_in', 'inc_q', 'fin37']]
    
    # received govt help
    government_help['received_govnt_help'] = government_help.apply(lambda x: 1 if x.fin37 == 1 else 0, axis = 1)
    government_help_17['received_govnt_help'] = government_help_17.apply(lambda x: 1 if x.fin37 == 1 else 0, axis = 1)
    
    
    # summarize
    income_data = government_help.groupby(['inc_q']).agg(total_population = ('wpid_random', 'count'),
                                                         total_received_help = ('received_govnt_help', 'sum')).reset_index()

    income_data_17 = government_help_17.groupby(['inc_q']).agg(total_population = ('wpid_random', 'count'),
                                                               total_received_help  = ('received_govnt_help', 'sum')).reset_index()
    
    income_data['% of population who received help'] = income_data['total_received_help']*100/income_data['total_population']
    income_data_17['% of population who received help'] = income_data_17['total_received_help']*100/income_data_17['total_population']
    
    custom_order = {'richest 20%': 0, 'fourth 20%':1, 'middle 20%':2,'second 20%' : 3, 'poorest 20%':4}

    income_data = income_data.sort_values(by = ['inc_q'], key = lambda x: x.map(custom_order))
    income_data_17 = income_data_17.sort_values(by = ['inc_q'], key = lambda x: x.map(custom_order))

    
    ####### Plot - 40% Y AXIS #######
    #create a subplot with small size
    fig, ax = plt.subplots(figsize=(8, 5), dpi = 200)
    
    ax.plot(income_data['inc_q'], 
            income_data['% of population who received help'],
            color = 'grey')
    
    ax.plot(income_data['inc_q'][-3:],
             income_data['% of population who received help'][-3:],
             color = '#007C80',
             linewidth = 2.5)
    ax.tick_params(left=0) 
    for location in ['right', 'top']:
            ax.spines[location].set_visible(False)
    
    ax.text( x = 2.9, y = 37, s = '36.6%', weight = 'normal', size = 10)
    ax.text( x = 4.03, y = 36, s = '35.67%', weight = 'normal', size = 10)
    ax.text( x = 1.8, y = 36.3, s = '35.96%', weight = 'normal', size = 10)
    ax.text( x = 0.9, y = 35, s = '34.31%', weight = 'normal', size = 10)
    ax.text( x = 0.1, y = 26.7, s = '26.57%', weight = 'normal', size = 10)
    
    ax.set_yticks([25, 35, 40])
    ax.set_yticklabels(['25%', '35%', '40%'])
    
    ax.set_ylabel('% Population')
    ax.set_xlabel('Household Income')
    ax.text(x = 0.0001, y = 40, s = '% of Filipinos who Received Help from the\nGovernment per Income Group', weight = 'bold',  size = 15)
    
    ax.set_yticks([28, 35, 40])
    
    st.markdown("Those who belong in the lower income groups are more likely are more likely to receive help from the government compared to those with higher income.")
    st.pyplot(fig)
    
    
    ####### Plot - 100% Y AXIS #######
    #create a subplot with small size
    fig1, ax1 = plt.subplots(figsize=(8, 5), dpi = 200)
    
    ax1.plot(income_data['inc_q'], 
            income_data['% of population who received help'],
            color = 'grey')
    
    ax1.tick_params(left=0) 
    for location in ['right', 'top']:
            ax1.spines[location].set_visible(False)
    
    
    ax1.plot(income_data['inc_q'][-3:],
             income_data['% of population who received help'][-3:],
             color = '#007C80',
             linewidth = 2.5)
    ax1.set_yticks([25, 50, 75, 100])
    ax1.set_yticklabels(['25%', '50%', '75%', '100%'])
    
    ax1.set_ylabel('% Population')
    ax1.set_xlabel('Household Income')
    
    ax1.text( x = 2.9, y = 38, s = '36.6%', weight = 'normal', size = 10)
    ax1.text( x = 4.03, y = 36, s = '35.67%', weight = 'normal', size = 10)
    ax1.text( x = 1.8, y = 37.3, s = '35.96%', weight = 'normal', size = 10)
    ax1.text( x = 0.9, y = 36, s = '34.31%', weight = 'normal', size = 10)
    ax1.text( x = 0.0001, y = 30.7, s = '26.57%', weight = 'normal', size = 10)
    ax1.set_yticks([25, 50, 100])
    
    #input title
    ax1.text(x = 0.0001, y = 100, s = '% of Filipinos who Received Help from the\nGovernment per Income Group', weight = 'bold',  size = 15)
    st.subheader("")
    st.markdown("While lower income groups in the Philippines are more likely to receive government assistance, the overall proportion of the population receiving aid remains low")
    st.pyplot(fig1)

    
    ####### Plot - 2017 vs 2021 #######
    #create a subplot with small size
    fig2, ax2 = plt.subplots(figsize=(8, 5), dpi = 200)
    
    ax2.plot(income_data['inc_q'], 
            income_data['% of population who received help'],
            color = '#007C80')
    
    ax2.plot(income_data_17['inc_q'], 
            income_data_17['% of population who received help'],
            color = 'grey',
            alpha = 0.8)
    
    ax2.tick_params(left=0) 
    for location in ['right', 'top']:
            ax2.spines[location].set_visible(False)
    
    
    #Set Axis Label names
    ax2.set_ylabel('% Population')
    ax2.set_yticks([30, 40])
    ax2.set_yticklabels(['30%', '40%'])
    
    ax2.set_xlabel('Household Income')
    
    #Manually Set Texxts
    ax2.text( x = 2.9, y = 37.5, s = '36.6%', weight = 'normal', size = 10)
    ax2.text( x = 2.9, y = 22, s = '23.12%', weight = 'normal', size = 10)
    ax2.text( x = 4.03, y = 36, s = '35.67%', weight = 'normal', size = 8)
    ax2.text( x = 4.03, y = 34.5, s = '34.89%', weight = 'normal', size = 8)
    ax2.text( x = 1.9, y = 21, s = '20.2%', weight = 'normal', size = 10)
    ax2.text( x = 1.8, y = 36.3, s = '35.96%', weight = 'normal', size = 10)
    ax2.text( x = 0.9, y = 21, s = '20.57%', weight = 'normal', size = 10)
    ax2.text( x = 0.9, y = 35, s = '34.31%', weight = 'normal', size = 10)
    ax2.text( x = 0.0001, y = 20.5, s = '19.7%', weight = 'normal', size = 10)
    ax2.text( x = 0.0001, y = 25.7, s = '26.57%', weight = 'normal', size = 10)
    
    ax2.text( x = 0.0001, y = 37.7, s = '2023', weight = 'bold', size = 20, color = '#007C80' )
    ax2.text( x = 3.5, y = 24, s = '2017', weight = 'bold', size = 20, color = 'grey' )
    
    ax2.text(x = 0.0001, y = 41, s = '2017 vs 2021: % of Filipinos who Received Help from the\nGovernment per Income Group', weight = 'bold',  size = 15)

    st.subheader("")
    st.markdown("""
                - Government assistance has improved in all income groups from 2017 to 2021
                - However, government reach to the lowest income group only slightly improved from 34.9% to 35.7%
                """)    
    st.pyplot(fig2)

    
def summary_recos():
    st.write('**<p style="font-size:36px;">Summary</p>**', unsafe_allow_html=True)
    st.markdown("""
                ##### - Those belonging in low income groups receive the highest government support however, government support barely improved from 2017 to 2021 and only averages at 35.3%
                ##### - More than half of those belonging in low-income groups and not receiving government support borrowed money and mostly for medical bills - citing insufficient funds
                """)
    
    st.title("")
    st.write('**<p style="font-size:36px;">Recommendations</p>**', unsafe_allow_html=True)
    
    ##### Awareness & Accessibility #####
    st.write('**<p style="font-size:26px; color:#007C80;" >1) Launch awareness and accessibility programs </p>**', unsafe_allow_html=True)
    
    ## Awareness
    st.write('**<p style="font-size:20px;"> Awareness </p>**', unsafe_allow_html=True)
    st.write('<p style="font-size:16px;"> Launch an information campaign to educate the public, especially the vulnerable sector, about the available financial assistance programs </p>', unsafe_allow_html=True)
    st.markdown("""
                - Ensure BSP Financial Literacy programs are implemented by LGUs
                - Leverage online platforms and personalities (e.g., TikTok)
                """)    
                
    ## Accessibility
    st.write('**<p style="font-size:20px;"> Awareness </p>**', unsafe_allow_html=True)
    st.write('<p style="font-size:16px;"> Launch Financial Inclusion assistance programs via digital and offline platforms </p>', unsafe_allow_html=True)
    st.markdown("""
                - Use of Sari-Sari stores aside from CVS to facilitate financial services (Maya Digi-Palenke)
                - Mobile financial app integration (e.g., GCash, Maya)
                """)                    
    st.image("recos_01.jpg")
    

    ##### Reach & Effectiveness #####
    st.title("")
    st.write('**<p style="font-size:26px; color:#007C80;" >2) Assess Government reach and effectiveness </p>**', unsafe_allow_html=True)
    
    ## Awareness
    st.write('**<p style="font-size:20px;"> Reach </p>**', unsafe_allow_html=True)
    st.write('<p style="font-size:16px;"> Assess who was given assistance and identify who have not benefited </p>', unsafe_allow_html=True)
    st.markdown("""
                - Note that only 33.8% of the Filipino population were given assistance
                """)    
                
    ## Accessibility
    st.write('**<p style="font-size:20px;"> Effectiveness </p>**', unsafe_allow_html=True)
    st.write('<p style="font-size:16px;"> Assess the demography with the highest need to focus on </p>', unsafe_allow_html=True)
    st.markdown("""
                - Income Bracket, Employment Status, Educational Background
                """)                    
    st.image("recos_02.jpg")
    
    
list_of_pages = [
    "Background",
    "Objective",
    "Low Income, High Need",
    "Assistance per Income Group",
    "Summary & Recommendations"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Background":
    introduction()
    
elif selection == "Objective":
    objective()

elif selection == "Low Income, High Need":
    govt_help_stats()

elif selection == "Assistance per Income Group":
    income_group()
    
elif selection == "Summary & Recommendations":
    summary_recos()