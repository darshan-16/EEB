import smtplib
from email.message import  EmailMessage
import database as vAR_db
import streamlit as vAR_st

def check_presence(optn):
    res = vAR_db.retrieve_frames()
    for code in res:
        if(code[0] + code[1] == 0):
            if (optn == 0):
                send_mail()
                vAR_st.text("Mail sent")
            if (optn == 1):
                send_sms()
                vAR_st.text("SMS sent")
            break

def send_mail():
    msg = EmailMessage()
    msg.set_content("No one in the frame")
    msg['subject'] = "Alert"
    msg['to'] = "darshanunofficial01@gmail.com"
    user = "alertmail73@gmail.com"
    msg['from'] = user
    password = "aafkmwpycwljhemp"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


def send_sms():
    msg = EmailMessage()
    msg.set_content("No one in the frame")
    msg['subject'] = "Alert"
    msg['to'] = "9162960228@txt.att.net"
    user = "alertmail73@gmail.com"
    msg['from'] = user
    password = "aafkmwpycwljhemp"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()