import cv2
import app
import numpy as np
from mtcnn import MTCNN
from Database.database import database as vAR_db
import streamlit as vAR_st
from deepface import DeepFace
from deepface.basemodels import VGGFace
from base64 import b64decode, b64encode
from deepface.extendedmodels import Race, Gender

mod = None
def model_pipeline():
    global mod
    mod = VGGFace.loadModel()
    Race.loadModel()
    Gender.loadModel()

def process_frames(df):
    vAR_db.truncateProTable()
    res = vAR_db.readImg()
    i = 0
    for code in res:
        i += 1
        data = b64decode(code[0])
        nparr = np.frombuffer(data, np.uint8)
        nparr.reshape(len(nparr),1)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        frame_process(img_np, df, i)

def frame_process(frame, df, i):
    global mod
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    det = MTCNN()
    face = det.detect_faces(img = img)
    race = []
    gender = []
    customer = []
    cid = []
    address = []
    phone = []
    email = []
    male = 0
    female = 0
    for f in face:
        x, y, width, height = f['box']
        (startX, startY) = x, y
        (endX, endY) = x+width, y+height
        face_crop = np.copy(frame[startY:endY,startX:endX])
        if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
            continue
        obj = DeepFace.analyze(np.array(face_crop,dtype=np.uint8), actions = ['gender', 'race'] ,enforce_detection=False)
        gender.append(obj['gender'])
        race.append(obj['dominant_race'])
        df1 = DeepFace.find(np.array(face_crop,dtype=np.uint8), db_path='/home/jupyter/Energy_efficiency/model',
                             model_name='VGG-Face', model=mod, enforce_detection=False)
        if(df1.shape[0]>0):
            name = str(df1.iloc[0].identity)
            name = name.split('/')
            if(name[6] not in customer):
                try:
                    customer.append(name[6])
                    df2 = df.loc[df['Property Manager/Owner Name']==name[6]]
                    address.append(df2.iloc[0]['Property Contact Address'])
                    phone.append(df2.iloc[0]['Property Contact Phone'])
                    email.append(df2.iloc[0]['Property Contact Email'])
                    cid.append(df2.iloc[0]['Property ID'])
                except:
                    pass
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0,155,255), 2)
        if(gender[-1] == 'Man'):
            male += 1
        else:
            female += 1
    _, buffer = cv2.imencode('.jpg', frame)
    im_bytes = buffer.tobytes()
    encodedJPG = b64encode(im_bytes)
    vAR_db.insertFrameData(encodedJPG, str(cid), str(customer), str(address), str(phone), str(email), str(race), male, female, i)
