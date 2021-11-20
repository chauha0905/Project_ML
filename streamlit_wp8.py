import streamlit as st
import pandas as pd
import cv2
import numpy as np 
import matplotlib as plt 
import tensorflow as tf 

menu = ['Home', 'All about', 'Projects', 'Camera', 'Music', 'Videos']

choice = st.sidebar.selectbox('MENU', menu)

if choice == 'Home':

    st.header("Welcome to the playground")
    st.text('This is a playground. All about my interests! Leave your signs after visiting!')

    st.image('media/Playground.jpg', caption= 'Can you swim?', use_column_width='auto')

    col1, col2 = st.columns(2)
    with col1:
        your_name = st.text_input("What's your name?")
        if your_name != '':
            st.write(your_name,' is a beautiful name')
    with col2:
        your_sport = st.text_input("Can you swim?")
        # if your_sport == 'No' or your_sport == 'no' or your_sport != 'NO' or your_sport == 'N' or your_sport == 'n':
        #     st.write("It's better if you can swim! You can save me in the pool")
        if your_sport != '':
            st.write("Great! I can't swim, so you can save me!")
        
#     col1, col2 = st.columns(2)
#     with col1:
#         dog_name = st.text_input("What's dog name?")
#         st.write('Your dog name: ', dog_name)    
#     with col2:
#         age = st.slider('Dog age', min_value = 1, max_value = 20)
#         st.write('Your dog age: ', age)

#     # dog_name = st.text_input("What's dog name?")
#     # st.write('Your dog name: ', dog_name)           # input từ người dùng 
    
#     # age = st.slider('Dog age', min_value = 1, max_value = 20)  # tạo slider kéo 
# elif choice == 'Read data':
#     df = pd.read_csv('media/AB_NYC_2019.csv')
#     st.dataframe(df)

# elif choice == 'About me':
#     # st.audio('media/Impact_Moderato.mp3')
#     fileUp = st.file_uploader('Your upload', type = ['jpg', 'jpeg', 'png'])   # max size = 200MB
#     st.image(fileUp)
#     # model.predict(fileUp)  # hint for weekly project, should resize / preprocessing before predict

# elif choice == 'Camera':
#     st.title('Open your webcam')
#     st.warning('Webcam show on local computer ONLY')
#     show = st.checkbox('Show!')
#     FRAME_WINDOW = st.image([])
#     camera = cv2.VideoCapture(0) # device 1/2

#     while show:
#         _, frame = camera.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         FRAME_WINDOW.image(frame)
#     else:
#         camera.release()

#     cam = cv2.VideoCapture(0) # device 0. If not work, try with 1 or 2

#     if not cam.isOpened():
#         raise IOError("Cannot open webcam")

#     while True:
#         ret, frame = cam.read()
#         frame = cv2.flip(frame, 1)
        
#         cv2.imshow('My App!', frame)

#         key = cv2.waitKey(1) & 0xFF
#         if key==ord("q"):
#             break

#     cam.release()
#     cv2.destroyAllWindows()