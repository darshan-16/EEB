import cv2
import DSAI_app
import numpy as np
from mtcnn import MTCNN
from DSAI_Data_Engineering.DSAI_Database.DSAI_database import database as vAR_db
import streamlit as vAR_st
from deepface import DeepFace
from deepface.basemodels import VGGFace
from base64 import b64decode, b64encode

def outcome_model():
    res = vAR_db.retrieve_frames()
    for row in res:
        data = b64decode(row[0])
        nparr = np.frombuffer(data, np.uint8)
        nparr.reshape(len(nparr),1)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        vAR_st.text("Name: " + str(row[2]))
        vAR_st.text("Race: " + str(row[6]))
        vAR_st.text("Male count: " + str(row[7]))
        vAR_st.text("Female count: " + str(row[8]))
        vAR_st.image(img_np, channels="BGR")