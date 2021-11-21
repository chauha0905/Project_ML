
import streamlit as st 
import pandas as pd
import cv2
import numpy as np 
import matplotlib as plt 
import tensorflow as tf 

menu = ['Home', 'All about', 'Entertainment', 'PicPred. RICH HOOMAN!', 'CamPred. PLAY FUN!']

choice = st.sidebar.selectbox('MENU', menu)

Model_Path = 'my_model_save.h5'
class_names = ['1000', '10000', '100000', '2000', '20000', '200000', '5000', '50000', '500000']
model = tf.keras.models.load_model(Model_Path)

if choice == 'Home':
    st.header("Welcome to the playground")
    st.text('This is a playground. All about my interests! Leave your signs after visiting!')

    st.image('media/vespa.png', caption= 'Which activity do you like?')
    
    your_name = st.text_input("What's your name?")
    if your_name != '':
        st.write(your_name,' is a beautiful name!')
        st.write(your_name, ", let's explore more in the next space. Have fun!")

elif choice == 'Entertainment':
    st.header('Freedom your soul here')
    st.image('media/Entertainment.png', caption = 'Play yoyr way!')

    st.video('media/Believer_Imagine Dragons.mp4')

    st.audio('media/EverythingSucks-Vaultboy.mp3')

elif choice == 'CamPred. PLAY FUN!':
    cap = cv2.VideoCapture(0)  # device 0
    run = st.checkbox('Show Webcam')
    capture_button = st.checkbox('Capture')

    captured_image = np.array(None)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    FRAME_WINDOW = st.image([])
    while run:
        ret, frame = cap.read()        
        # Display Webcam
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)          #Convert color
        FRAME_WINDOW.image(frame)

        if capture_button:      
            captured_image = frame
            break

    cap.release()

    if  captured_image.all() != None:
        st.image(captured_image)
        st.write('Image is captured:')
        
        captured_image = cv2.resize(captured_image, (224,224))  #Resize Image according to model
        img_array  = np.expand_dims(captured_image, axis=0)     #Resize Image according to model
        # st.write(img_array)                                   #Check the img_array here (no_use this line)
        prediction = model.predict(img_array)
        index = np.argmax(prediction.flatten())
        st.write('You money is:', class_names[index])

elif choice == 'PicPred. RICH HOOMAN!':
    st.image('media/VND_banknotes.png', caption='Such a rich one! Show your money here!')

    photo_uploaded = st.file_uploader('Upload your money', ['png', 'jpeg', 'jpg'])
    if photo_uploaded != None:
        image_np = np.asarray(bytearray(photo_uploaded.read()), dtype=np.uint8)
        img = cv2.imdecode(image_np, 1)
        st.image(img, channels='BGR')
        captured_image = cv2.resize(img, (224,224))
        #Expand dim
        img_array  = np.expand_dims(img, axis=0)
        #Prediction
        prediction = model.predict(img_array)
        index = np.argmax(prediction.flatten())
        st.write('You money is:', class_names[index])
