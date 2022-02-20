import html
import process_frames as vAR_pf
import capture_frames as vAR_cfu
import model_outcome as vAR_mo
import visual as vAR_vu
import pandas as pd
import streamlit as vAR_st
import alert as vAR_alert
import streamlit.components.v1 as components
from IPython.display import HTML
from bokeh.models.widgets import Div


if __name__ == '__main__':
    vAR_st.set_page_config(layout="wide")
    
    col1, col2, col3 = vAR_st.columns([2, 5, 2])
    with col1:
        vAR_st.write('')
    with col2:
        vAR_st.image('https://raw.githubusercontent.com/tarun243/Streamlit-commonToAllIndustry/master/Web_app/Logo_final.png')
    with col3:
        vAR_st.write('')

    vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px; '>ENERGY EFFICIENCY AND ENERGY BENCH MARKING </h1>", unsafe_allow_html=True)

    vAR_st.markdown("<p style='text-align: center; color: blue; font-size:29px;'>MLOPS Built On Google Cloud and Streamlit</p>", unsafe_allow_html=True)

    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Develop Machine Learning Applications (MLOPS) for energy efficiency: Optimize energy usage, reduce energy consumption and energy cost</p>", unsafe_allow_html=True)

    #for background color of sidebar
    #for text box
    #for clear/reset button
    #To customize the background colour of the submit button
    vAR_st.markdown("""<style>
    a {
        text-decoration: none;
    }
    .css-1d391kg, .e1fqkh3o1{
        background-color: #4c85e4;
        width: 19rem;
    }
    .css-10trblm{
        box-shadow: 0 2px 8px 0 #35353533;
        padding: 10px 30px;
        font-size: 20px;
    }
    #energy-efficiency-and-energy-bench-marking>.css-f341up>.css-10trblm{
        box-shadow: none;
        padding: none;
        font-size: 25px;
    }
    h3{
        padding: 0.3rem 0px 0.9rem;
    }
    .button{
        background-color:rgb(47 236 106);  
        top: 40px; 
        border: 0px solid; 
        padding: 10px;
        border-radius:3px;
    }
    p, ol, ul, dl {
        margin: 10px 80px 1rem;
        font-size: 1rem;
        font-weight: 400;
    }
    div.stButton > button:first-child{
        border: 1px solid; width: 55%;
        background-color: rgb(47 236 106) ;
    }
    </style>""", unsafe_allow_html=True)

    #for horizontal line
    vAR_st.markdown("""
    <hr style="width:100%;height:3px;background-color:gray;border-width:10">
    """, unsafe_allow_html=True)

    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
    
    with _:
        vAR_st.write('')

    with col4:
        vAR_st.write('')

    with col2:
        vAR_st.write('')
        vAR_st.write('')
        vAR_st.subheader("Data Source")
    
    with col3:
        vAR_datasource = vAR_st.selectbox('',('Select the source', 'Camera', 'Youtube'),index=0)
    
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
    
    with _:
        vAR_st.write('')

    with col2:
        vAR_st.write('')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource == 'Youtube':
            if 'f' not in vAR_st.session_state:
                vAR_st.session_state.f = False
            url = vAR_st.text_input('Enter the Youtube URL')
        if vAR_datasource == 'Camera':
            if 'f' not in vAR_st.session_state:
                vAR_st.session_state.f = False
            val = vAR_st.text_input('Enter the Camera URL')

    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
    
    with _:
        vAR_st.write('')

    with col2:
        vAR_st.write('')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource == 'Youtube':
            if (url!='') and (not vAR_st.session_state.f):
                #vAR_cfu.check_url(url)
                vAR_st.text(str(url))
                vAR_st.session_state.f = True
        if vAR_datasource == 'Camera':
            if (val!='') and (not vAR_st.session_state.f):
                vAR_st.text(str(val))
                vAR_st.session_state.f = True

    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
    
    with _:
        vAR_st.write('')

    with col2:
        vAR_st.write('')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if 'vu' not in vAR_st.session_state:
                    vAR_st.session_state.vu = False
                vAR_validate = vAR_st.button("Validate URL")
                if vAR_validate and vAR_datasource == 'Camera':
                    vAR_st.text("Surveillance Camera URL Reachable")
                    vAR_st.text("Valid URL")
                    vAR_st.session_state.vu = True
                elif vAR_validate and vAR_datasource == 'Youtube':
                    vAR_st.text("Youtube URL Reachable")
                    vAR_st.text("Valid URL")
                    vAR_st.session_state.vu = True

    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')

    with _:
        vAR_st.write('')
        
    with col4:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and  (vAR_st.session_state.vu != False):
                vAR_st.subheader('Data Streaming')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and  (vAR_st.session_state.vu != False):
                if 'dp' not in vAR_st.session_state:
                    vAR_st.session_state.dp = False
                vAR_datapipeline = vAR_st.button("Start Data Pipeline (Streaming)")

        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and  (vAR_st.session_state.vu != False):
                stop = vAR_st.button("Stop Data Streaming")
                if stop:
                    vAR_st.session_state.dp = True
    
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')

    with _:
        vAR_st.write('')
        
    with col4:
        vAR_st.write('')

    with col2:
        vAR_st.write('')
        
    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and  (vAR_st.session_state.vu != False):
                if vAR_datapipeline:
                    if vAR_datasource=='Youtube':
                        vAR_cfu.capture_frames_cam(url, stop)
                        vAR_st.session_state.dp = True
                    if vAR_datasource=='Camera':
                        vAR_cfu.capture_frames_cam(val,stop)
                        vAR_st.session_state.dp = True
    
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')

    with _:
        vAR_st.write('')
        
    with col4:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    vAR_st.subheader('Data Engineering')
        
    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if 'de' not in vAR_st.session_state:
                        vAR_st.session_state.de = False
                    vAR_dataengineer = vAR_st.button("Start Data Engineering")
                    if vAR_dataengineer:
                        vAR_st.session_state.de = True
    
    vAR_st.write('')
    col1, col2, _ = vAR_st.columns([1, 6, 1])
    with col1:
        vAR_st.write('')

    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        vAR_customers = vAR_st.file_uploader("Upload Customer Demographic Data")
    
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        vAR_st.write('')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            df_customers = pd.read_csv(vAR_customers)
                            df = df_customers.astype(str)
                            if 'pv' not in vAR_st.session_state:
                                vAR_st.session_state.pv = False
                            vAR_preview = vAR_st.button("Preview data")
                            if vAR_preview:
                                vAR_st.session_state.pv = True
    
    col1, col2, col3 = vAR_st.columns([1, 4, 1])
    with col1:
        vAR_st.write('')

    with col3:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.pv:
                                vAR_st.table(df_customers)
    
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            vAR_st.subheader('Feature Selection')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if 'fs' not in vAR_st.session_state:
                                vAR_st.session_state.fs = False
                            vAR_featureselection = vAR_st.multiselect("Feature Selection for Gender Classifiction & Facial Recognition", ['Eyes', 'Ears', 'Nose', 'Mouth', 'Chin', 'Color', 'Weight', 'Height'])
    
    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if 'fs' not in vAR_st.session_state:
                                vAR_st.session_state.fs = False
                            vAR_st.text(" ")
                            vAR_submit = vAR_st.button("Submit", key="1")
                            if vAR_submit:
                                vAR_st.session_state.fs = True
    
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                vAR_st.subheader('Hyper Parameter Tuning')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if 'hp' not in vAR_st.session_state:
                                    vAR_st.session_state.hp = False
                                vAR_hyperparametertune_ac = vAR_st.multiselect("Hyper parameter(action)", ['Age', 'Gender', 'Race', 'Emotion'])

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if 'hp' not in vAR_st.session_state:
                                    vAR_st.session_state.hp = False
                                vAR_hyperparametertune_md = vAR_st.selectbox("Hyper parameter(model)", ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"])
    
    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if 'hp' not in vAR_st.session_state:
                                    vAR_st.session_state.hp = False
                                vAR_submit_hp = vAR_st.button("Submit", key="2")
                                if vAR_submit_hp:
                                    vAR_st.session_state.hp = True
    
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    vAR_st.subheader('Model Pipeline')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if 'mp' not in vAR_st.session_state:
                                        vAR_st.session_state.mp = False
                                    vAR_modelpipeline = vAR_st.button("Start Model Pipeline")
                                    if vAR_modelpipeline:
                                        vAR_pf.model_pipeline()
                                        vAR_st.session_state.mp = True
                                    if vAR_st.session_state.mp == True:
                                        vAR_st.text("Done")
    
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        vAR_st.subheader('Model Engineering')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if 'me' not in vAR_st.session_state:
                                            vAR_st.session_state.me = False
                                        vAR_modelengineer = vAR_st.button("Start Model Engineering")
                                        if vAR_modelengineer:
                                            vAR_pf.process_frames(df)
                                            vAR_st.session_state.me = True
                                        if vAR_st.session_state.me == True:
                                            vAR_st.text("Done")
    
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            vAR_st.subheader('Model Outcome')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if 'mo' not in vAR_st.session_state:
                                                vAR_st.session_state.mo = False
                                            vAR_modeloutcome = vAR_st.button("Review Model Outcome")
                                            if vAR_st.session_state.mo == True:
                                                vAR_st.text("Done")
    
    col1, col2, col3 = vAR_st.columns([1, 5, 1])
    with col1:
        vAR_st.write('')

    with col3:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if 'mo' not in vAR_st.session_state:
                                                vAR_st.session_state.mo = False
                                            if vAR_modeloutcome:
                                                vAR_mo.outcome_model()
                                                vAR_st.session_state.mo = True

    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if vAR_st.session_state.mo != False:
                                                vAR_st.subheader('Alert Notification')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if vAR_st.session_state.mo != False:
                                                if 'an' not in vAR_st.session_state:
                                                    vAR_st.session_state.an = False
                                                vAR_analyze_e = vAR_st.button("Alert Notification to the Property Manager: Email")
                                                if vAR_analyze_e:
                                                    vAR_alert.check_presence(0)
                                                    vAR_st.session_state.an = True
                                                if vAR_st.session_state.an == True and vAR_analyze_e:
                                                    vAR_st.text("Done")
                                                vAR_analyze_s = vAR_st.button("Alert Notification to the Property Manager: Text")
                                                if vAR_analyze_s:
                                                    vAR_alert.check_presence(1)
                                                    vAR_st.session_state.an = True
                                                if vAR_st.session_state.an == True and vAR_analyze_s:
                                                    vAR_st.text("Done")
    col1, col2, col3 = vAR_st.columns([1, 5, 1])
    with col1:
        vAR_st.write('')

    with col3:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if vAR_st.session_state.mo != False:
                                                if vAR_analyze_e:
                                                    vAR_st.image('/home/jupyter/Energy_efficiency/Pics_alert/email.png')
                                                if vAR_analyze_s:
                                                    vAR_st.image('/home/jupyter/Energy_efficiency/Pics_alert/sms.png')
    
    menu = ["MLOps Components","Data Source","Data Pipeline","Data Engineering","Model Pipeline","Model Engineering","Model Outcome","Analysis","Visualization"]
    choice = vAR_st.sidebar.selectbox(" ",menu)

    library = ["Library Used","Streamlit","OpenCV","Pandas","iPython.display","Deepface","Numpy","EmailMessage","Pyplot","Pafy"]
    lib = vAR_st.sidebar.selectbox(" ",library)

    models_implemented = ['Models Implemented','DeepFace - Gender Detection','DeepFace - Race Detection','DeepFace - VGGFace']
    mi = vAR_st.sidebar.selectbox(" ",models_implemented)

    services = ["GCP Services Used","IOT core", "Cloud storage", "Pub/sub", "Google cloud Dataflow", "Cloud Storage", "BigQuery", "Vertex AI - AutoML", "Vision AI", "AI Platform", "Google Datastudio", "Looker"]
    gcp = vAR_st.sidebar.selectbox(" ",services)


    href = f'<a style="color:black;" href="" class="button">Clear/Reset</a>'
    vAR_st.sidebar.markdown(href, unsafe_allow_html=True)

    vAR_st.write('')
    vAR_st.write('')
    col1, col2, _, col3, col4 = vAR_st.columns([1, 2, 1, 3, 1])
    with col1:
        vAR_st.write('')
        
    with _:
        vAR_st.write('')

    with col2:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if vAR_st.session_state.mo != False:
                                                if vAR_st.session_state.an != False:
                                                    vAR_st.subheader('Data Visualization')

    with col4:
        vAR_st.write('')

    with col3:
        if vAR_datasource != 'Select the source':
            if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if vAR_st.session_state.mo != False:
                                                if vAR_st.session_state.an != False:
                                                    if 'dv' not in vAR_st.session_state:
                                                        vAR_st.session_state.dv = False
                                                    vAR_visualize = vAR_st.button("Analyze data")
                                                    vAR_visualize_ui = vAR_st.button("Model outcome")

    if vAR_datasource != 'Select the source':
        if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
            if vAR_st.session_state.dp != False:
                if vAR_st.session_state.de != False:
                    if vAR_customers is not None:
                        if vAR_st.session_state.fs != False:
                            if vAR_st.session_state.hp != False:
                                if vAR_st.session_state.mp != False:
                                    if vAR_st.session_state.me != False:
                                        if vAR_st.session_state.mo != False:
                                            if vAR_st.session_state.an != False:
                                                if vAR_visualize:
                                                    js = "window.open('https://datastudio.google.com/u/1/reporting/be413248-bb74-4c1b-bf4a-69dde8a9a637/page/WsMEC')"  # New tab or window
                                                    html = '<img src onerror="{}">'.format(js)
                                                    div = Div(text=html)
                                                    vAR_st.bokeh_chart(div)
                                                    vAR_st.session_state.dv = True
    
    if vAR_datasource != 'Select the source':
        if (vAR_st.session_state.f != False) and (vAR_st.session_state.vu != False):
            if vAR_st.session_state.dp != False:
                if vAR_st.session_state.de != False:
                    if vAR_customers is not None:
                        if vAR_st.session_state.fs != False:
                            if vAR_st.session_state.hp != False:
                                if vAR_st.session_state.mp != False:
                                    if vAR_st.session_state.me != False:
                                        if vAR_st.session_state.mo != False:
                                            if vAR_st.session_state.an != False:
                                                if vAR_visualize_ui:
                                                    vAR_vu.visualize()
                                                    vAR_st.session_state.dv = True
