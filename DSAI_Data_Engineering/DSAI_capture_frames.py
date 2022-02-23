import re
import cv2
import DSAI_app
import pafy
import urllib
import requests
import numpy as np
from DSAI_Data_Engineering.DSAI_Database.DSAI_database import database as vAR_db
import streamlit as vAR_st
from base64 import b64decode, b64encode

class capture_frames:
    def check_url(url):
        reg = "^((?:https?:\/\/))?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(watch\?(.*&)?v=\/?))([^\?\&\"\'>]+)$"
        url = str(url)
        vAR_st.write(url)
        if re.match(reg, url):
            x = requests.get(url)
            if("Video unavailable" in x.text):
                vAR_st.text("Video unavailable")
                vAR_st.session_state.f = False
                return
            vAR_st.text("URL verified")
            vAR_st.session_state.f = True
        else:
            vAR_st.write("URL not valid")
            vAR_st.session_state.f = False

    def capture_frames_url(url, stop):
        if url!='':
            if not stop:
                url = str(url)
                video = pafy.new(url, )
                best  = video.getbest(preftype="mp4")
                cap = cv2.VideoCapture(best.url)
                vAR_db.truncateTable()
                i = 0
                while True:
                    i += 1
                    ret, frame = cap.read()
                    _, buffer = cv2.imencode('.jpg', frame)
                    im_bytes = buffer.tobytes()
                    encodedJPG = b64encode(im_bytes)
                    vAR_db.insertFrame(encodedJPG, i)
                    if stop:
                        break
                cap.release()
                cv2.destroyAllWindows()

    def capture_frames_cam(val,stop):
        if val!='':
            if not stop:
                url = str(val)
                cap = cv2.VideoCapture(url)
                vAR_db.truncateTable()
                i = 0
                while True:
                    i += 1
                    ret, frame = cap.read()
                    _, buffer = cv2.imencode('.jpg', frame)
                    im_bytes = buffer.tobytes()
                    encodedJPG = b64encode(im_bytes)
                    vAR_db.insertFrame(encodedJPG, i)
                    if stop:
                        break
                cap.release()
                cv2.destroyAllWindows()