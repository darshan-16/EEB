import pandas as pd
import streamlit as vAR_st
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def visualize():
    vAR_st.write('')
    vAR_st.write('')
    data = {"#":["Energy Requirements for Cooling", "Energy Requirements for Cooling per unitarea", "Energy Requirements for Heating", "Energy Requirements for Heating per unitarea", 
            "Energy Requirements for Lighting", "Energy Requirements for Lighting per unitarea", "Energy Requirements for Water Supply", "Energy Requirements for Water Supply per unitarea"],
        "Total":[31474.2, 169.6, 33215.6, 178.5, 15245.0, 82.3, 29907.0, 161.0],
        "Jan":[0.0, 0.0, 6985.5, 37.6, 964.9, 5.2, 2161.7, 11.6],
        "Feb":[0.0, 0.0, 7503.4, 40.4, 1374.3, 7.4, 2641.7, 14.3],
        "Mar":[1208.6, 6.5, 2999.9, 16.1, 1117.3, 6.0, 2161.7, 11.6],
        "Apr":[2165.9, 11.6, 1646.6, 8.8, 1511.7, 8.2, 2830.3, 15.3],
        "May":[2077.0, 11.2, 0.0, 0.0, 1015.7, 5.4, 2161.7, 11.6],
        "Jun":[5800.8, 31.3, 0.0, 0.0, 1511.7, 8.2, 2830.3, 15.3],
        "Jul":[5825.7, 31.4, 0.0, 0.0, 1168.1, 6.3, 2161.7, 11.6],
        "Aug":[8343.7, 45.0, 0.0, 0.0, 1442.9, 7.8, 2924.7, 15.7],
        "Sep":[3801.6, 20.5, 0.0, 0.0, 1117.3, 6.0, 2091.9, 11.3],
        "Oct":[2250.9, 12.1, 1499.7, 8.0, 1442.9, 7.8, 2924.7, 15.7],
        "Nov":[0.0, 0.0, 3667.7, 19.7, 1066.5, 5.8, 2091.9, 11.3],
        "Dec":[0.0, 0.0, 8912.8, 47.9, 1511.7, 8.2, 2924.7, 15.7]}
    preprocess(data, 0)

    vAR_st.write('')
    data1 = {"#":["Energy Requirements for Cooling", "Energy Requirements for Cooling per unitarea", "Energy Requirements for Heating", "Energy Requirements for Heating per unitarea", 
            "Energy Requirements for Lighting", "Energy Requirements for Lighting per unitarea", "Energy Requirements for Water Supply", "Energy Requirements for Water Supply per unitarea"],
        "Total":[13284.6, 71.3, 24118.3, 129.8, 11726.8, 62.9, 29907.0, 161.0],
        "Jan":[0.0, 0.0, 4920.6, 26.5, 742.3, 4.0, 2161.7, 11.6],
        "Feb":[0.0, 0.0, 5297.5, 28.5, 1057.1, 5.7, 2641.7, 14.3],
        "Mar":[306.0, 1.6, 2187.5, 11.8, 859.4, 4.6, 2161.7, 11.6],
        "Apr":[727.3, 3.9, 1498.6, 8.0, 1162.8, 6.2, 2830.3, 15.3],
        "May":[847.4, 4.6, 0.0, 0.0, 781.3, 4.2, 2161.7, 11.6],
        "Jun":[2487.7, 13.3, 0.0, 0.0, 1162.8, 6.2, 2830.3, 15.3],
        "Jul":[2708.2, 14.6, 0.0, 0.0, 898.5, 4.8, 2161.7, 11.6],
        "Aug":[3917.5, 21.0, 0.0, 0.0, 1110.0, 6.0, 2924.7, 15.7],
        "Sep":[1552.3, 8.3, 0.0, 0.0, 859.4, 4.6, 2091.9, 11.3],
        "Oct":[738.2, 4.0, 1438.1, 7.7, 1110.0, 6.0, 2924.7, 15.7],
        "Nov":[0.0, 0.0, 2546.9, 13.7, 820.4, 4.4, 2091.9, 11.3],
        "Dec":[0.0, 0.0, 6229.1, 33.6, 1162.8, 6.2, 2924.7, 15.7]}
    preprocess(data1, 1)

    data3 = {"Current density":[10, 13, 25, 31, 36, 47, 52, 58, 61, 67, 80, 99],
             "Energy Efficiency":[0.26, 0.299, 0.30, 0.31, 0.312, 0.321, 0.378, 0.35, 0.39, 0.356, 0.31, 0.284],
             "Optimized Energy Efficiency":[0.56, 0.599, 0.621, 0.61, 0.612, 0.632, 0.68, 0.66, 0.68, 0.667, 0.61, 0.590]}
    
    data4 = {"Current density":[10, 13, 25, 31, 36, 47, 52, 58, 61, 67, 80, 99],
             "Energy Efficiency":[0.1, 0.12, 0.14, 0.15, 0.17, 0.19, 0.185, 0.18, 0.16, 0.156, 0.139, 0.119],
             "Optimized Energy Efficiency":[0.2, 0.22, 0.24, 0.25, 0.27, 0.29, 0.285, 0.28, 0.26, 0.256, 0.239, 0.219]}
    efficiency_graph(data3, data4)

def efficiency_graph(data, data1):
    df1 = pd.DataFrame(data)
    df1.set_index('Current density', inplace=True)

    df2 = pd.DataFrame(data1)
    df2.set_index('Current density', inplace=True)

    vAR_st.write('')
    vAR_st.write('')
    vAR_st.write('')
    vAR_st.write('')
    col1, col2, col3 = vAR_st.columns([1, 5, 1])
    with col1:
        vAR_st.write('')
    
    with col2:
        vAR_st.title("Optimized Energy Consumption | Energy Usage Before and After Energy Efficiency")
        vAR_st.line_chart(df1)

    with col3:
        vAR_st.write('')
    
    vAR_st.write('')
    vAR_st.write('')
    vAR_st.write('')
    col1, col2, col3 = vAR_st.columns([1, 5, 1])
    with col1:
        vAR_st.write('')
    
    with col2:
        vAR_st.title("Optimized Energy Consumption | Energy Usage Before and After Energy Efficiency")
        vAR_st.line_chart(df2)

    with col3:
        vAR_st.write('')

def preprocess(data, op):
    vAR_st.write('')
    vAR_st.write('')
    df1 = pd.DataFrame(data)
    df2 = df1.loc[[1, 3, 5, 7]]
    df2.reset_index(inplace=True)
    df2.drop(['index'], axis=1, inplace=True)
    df2['#'][0] = 'Energy Requirements for Cooling'
    df2['#'][1] = 'Energy Requirements for Heating'
    df2['#'][2] = 'Energy Requirements for Lighting'
    df2['#'][3] = 'Energy Requirements for Water Supply'
    df3 = df2.set_index('#')
    df3 = df3.transpose()
    df3.drop('Total', axis=0, inplace=True)
    df4 = df3.reset_index()

    if(op!=1):
        col1, col2, col3 = vAR_st.columns([1, 5, 1])
        with col1:
            vAR_st.write('')

        with col2:
            fig = plt.figure(figsize=[4, 4])
            ax = fig.add_axes([0,0,1,1])
            ax.axis('equal')
            labels = ["Energy Requirements for Cooling", "Energy Requirements for Heating", "Energy Requirements for Lighting", "Energy Requirements for Water Supply"]
            ax.pie(df2["Total"], labels = labels,autopct='%1.2f%%', counterclock=False, colors=['#6050DC', '#D52DB7', '#FF6B45', '#FFAB05'])
            plt.title("Energy Requirement Distribution", size=32, fontweight="bold")
            vAR_st.pyplot(fig)

        with col3:
            vAR_st.write('')

        vAR_st.write('')
        vAR_st.write('')
        col1, col2, col3 = vAR_st.columns([1, 5, 1])
        with col1:
            vAR_st.write('')

        with col2:
            fig1 = plt.figure(figsize=[10,6])
            plt.bar(df4['index'], df3['Energy Requirements for Cooling'], color='#6050DC')
            plt.bar(df4['index'], df3['Energy Requirements for Heating'], bottom=df3['Energy Requirements for Cooling'], color='#D52DB7')
            plt.bar(df4['index'], df3['Energy Requirements for Lighting'], bottom=df3['Energy Requirements for Cooling']+df3['Energy Requirements for Heating'], color='#FF6B45')
            plt.bar(df4['index'], df3['Energy Requirements for Water Supply'], bottom=df3['Energy Requirements for Cooling']+df3['Energy Requirements for Heating']+df3['Energy Requirements for Lighting'], color='#FFAB05')
            plt.legend(["Energy Requirements for Cooling", "Energy Requirements for Heating", "Energy Requirements for Lighting", "Energy Requirements for Water Supply"])
            vAR_st.pyplot(fig1)

        with col3:
            vAR_st.write('')

    vAR_st.write('')
    vAR_st.write('')
    col1, col2, col3 = vAR_st.columns([1, 5, 1])
    with col1:
        vAR_st.write('')
    
    with col3:
        vAR_st.write('')

    with col2:
        if op==0:
            vAR_st.title("Energy Consumption - Before Efficiency")
        if op==1:
            vAR_st.title("Energy Consumption - After Efficiency")
        vAR_st.dataframe(df1)