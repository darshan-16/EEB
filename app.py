import html
import process_frames as vAR_pf
import capture_frames as vAR_cfu
import model_outcome as vAR_mo
import pandas as pd
import streamlit as vAR_st
import alert as vAR_alert
import streamlit.components.v1 as components
from IPython.display import HTML

if __name__ == '__main__':
    vAR_st.set_page_config(layout="wide")
    col1, col2, col3 = vAR_st.columns([3,5,3])
    with col2:
        vAR_st.image('https://raw.githubusercontent.com/tarun243/Streamlit-commonToAllIndustry/master/Web_app/Logo_final.png')

    vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px;'>ENERGY EFFICIENCY AND ENERGY BENCH MARKING </h1>", unsafe_allow_html=True)

    vAR_st.markdown("<h1 style='text-align: center; color: blue; font-size:29px;'>Powered by Google Cloud and Streamlit</h1>", unsafe_allow_html=True)

    vAR_st.markdown("""<style>a {
        text-decoration: none;
    }
    </style>""", unsafe_allow_html=True)

    #To customize the background colour of the submit button
    m = vAR_st.markdown("""
    <style>
    div.stButton > button:first-child {border: 1px solid; width: 55%;
        background-color: rgb(47 236 106) ;
    }
    </style>""", unsafe_allow_html=True)

    #for horizontal line
    vAR_st.markdown("""
    <hr style="width:100%;height:3px;background-color:gray;border-width:10">
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = vAR_st.columns([1, 2, 3, 1])
    with col2:
        vAR_st.write('')
        vAR_st.write('')
        vAR_st.subheader("Data source")
    
    with col3:
        vAR_datasource = vAR_st.selectbox('',('Select the source', 'Camera', 'Youtube'),index=0)
    
    vAR_st.write('')
    col1, col2, col3, col4 = vAR_st.columns([1, 3, 2, 1])
    with col2:
        if vAR_datasource == 'Youtube':
            if 'f' not in vAR_st.session_state:
                vAR_st.session_state.f = False
            url = vAR_st.text_input('Enter the Youtube URL')
        if vAR_datasource == 'Camera':
            if 'f' not in vAR_st.session_state:
                vAR_st.session_state.f = False
            val = vAR_st.text_input('Enter the Camera URL')

    col1, col2, col3, col4 = vAR_st.columns([1, 3, 2, 1])
    with col2:
        if vAR_datasource == 'Youtube':
            if (url!='') and (not vAR_st.session_state.f):
                vAR_st.text(str(url))
                #vAR_cfu.check_url(url)
                vAR_st.session_state.f = True
        if vAR_datasource == 'Camera':
            if (val!='') and (not vAR_st.session_state.f):
                vAR_st.text(str(val))
                vAR_st.session_state.f = True

    vAR_st.write('')
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if 'dp' not in vAR_st.session_state:
                    vAR_st.session_state.dp = False
                vAR_datapipeline = vAR_st.button("Start Data pipeline")

    with col3:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                stop = vAR_st.button("Stop")
                if stop:
                    vAR_st.session_state.dp = True
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_datapipeline:
                    if vAR_datasource=='Youtube':
                        vAR_cfu.capture_frames_cam(url, stop)
                        vAR_st.session_state.dp = True
                    if vAR_datasource=='Camera':
                        vAR_cfu.capture_frames_cam(val,stop)
                        vAR_st.session_state.dp = True
    
    vAR_st.write('')
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if 'de' not in vAR_st.session_state:
                        vAR_st.session_state.de = False
                    vAR_dataengineer = vAR_st.button("Start Data engineering")
                    if vAR_dataengineer:
                        vAR_st.session_state.de = True
    
    vAR_st.write('')
    col1, col2, col3, col4 = vAR_st.columns([1, 3, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        vAR_customers = vAR_st.file_uploader("Upload CSV file")
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            df_customers = pd.read_csv(vAR_customers, names=['cid', 'name', 'phone', 'city'])
                            df = df_customers.astype(str)
                            if 'pv' not in vAR_st.session_state:
                                vAR_st.session_state.pv = False
                            vAR_preview = vAR_st.button("Preview data")
                            if vAR_preview:
                                vAR_st.session_state.pv = True
    
    col1, col2, col3 = vAR_st.columns([1, 4, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.pv:
                                vAR_st.table(df_customers)
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if 'fs' not in vAR_st.session_state:
                                vAR_st.session_state.fs = False
                            vAR_featureselection = vAR_st.multiselect("Feature selection", ['Eyes', 'Ears', 'Nose', 'Mouth', 'Chin'])
    
    with col3:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if 'fs' not in vAR_st.session_state:
                                vAR_st.session_state.fs = False
                            vAR_st.text(" ")
                            vAR_submit = vAR_st.button("Submit", key="1")
                            if vAR_submit:
                                vAR_st.session_state.fs = True
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if 'hp' not in vAR_st.session_state:
                                    vAR_st.session_state.hp = False
                                vAR_hyperparametertune_ac = vAR_st.multiselect("Hyper parameter(action)", ['age', 'gender', 'race', 'emotion'])
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if 'hp' not in vAR_st.session_state:
                                    vAR_st.session_state.hp = False
                                vAR_hyperparametertune_md = vAR_st.selectbox("Hyper parameter(model)", ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"])
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if 'hp' not in vAR_st.session_state:
                                    vAR_st.session_state.hp = False
                                vAR_submit_hp = vAR_st.button("Submit", key="2")
                                if vAR_submit_hp:
                                    vAR_st.session_state.hp = True
    
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
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
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
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
    
    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
                if vAR_st.session_state.dp != False:
                    if vAR_st.session_state.de != False:
                        if vAR_customers is not None:
                            if vAR_st.session_state.fs != False:
                                if vAR_st.session_state.hp != False:
                                    if vAR_st.session_state.mp != False:
                                        if vAR_st.session_state.me != False:
                                            if 'mo' not in vAR_st.session_state:
                                                vAR_st.session_state.mo = False
                                            vAR_modeloutcome = vAR_st.button("Model Outcome")
                                            if vAR_st.session_state.mo == True:
                                                vAR_st.text("Done")
    
    col1, col2, col3 = vAR_st.columns([1, 5, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
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

    col1, col2, col3, col4 = vAR_st.columns([1, 2, 2, 1])
    with col2:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
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
                                                vAR_analyze = vAR_st.button("Send alert mail")
                                                if vAR_analyze:
                                                    vAR_alert.check_presence(0)
                                                    vAR_st.session_state.an = True
                                                if vAR_st.session_state.an == True:
                                                    vAR_st.text("Done")
    with col3:
        if vAR_datasource != 'Select the source':
            if vAR_st.session_state.f != False:
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
                                                vAR_analyze = vAR_st.button("Send sms")
                                                if vAR_analyze:
                                                    vAR_alert.check_presence(1)
                                                    vAR_st.session_state.an = True
                                                if vAR_st.session_state.an == True:
                                                    vAR_st.text("Done")