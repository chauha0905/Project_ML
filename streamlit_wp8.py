
import streamlit as st 
import pandas as pd
import cv2 
import numpy as np 
import matplotlib as plt 
import tensorflow as tf 

menu = ['The Playground', 'PicPred', 'CamPred', 'Entertainment']

choice = st.sidebar.selectbox('Homebox', menu)

Model_Path = 'my_model_save.h5'
class_names = ['1000', '10000', '100000', '2000', '20000', '200000', '5000', '50000', '500000']
model = tf.keras.models.load_model(Model_Path)

if choice == 'The Playground':
    st.title("T h e P l a y g r o u n d")
    st.text('Leave your signs after visiting!')

    # st.image('media/vespa.png', caption = 'Which activities do you like?')
    
    st.text('')
    col1, col2 = st.beta_columns([2,1])
    with col1:
        st.image('media/Playground.gif')
        st.subheader('Hi.')
    with col2:
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        your_name = st.text_input("What's your name?")
        if your_name != '':
            st.write(your_name,' is a beautiful name. \a Have a good day!')

elif choice == 'Entertainment':
    st.title('Freedom your soul')
    st.image('media/thumb.gif')
    st.subheader('\t Play your way!',)
    st.text('')
    st.text('')
    st.audio('media/EverythingSucks-Vaultboy.mp3')
    st.text('Everything sucks _ Vaultboy')
    st.text('')
    st.text('')

    col1, col2 = st.beta_columns(2)
    with col1:
        st.video('media/Believer - Cover.mp4')
        st.text('Believer_Cover by Kids')
    with col2:
        st.video('media/Imagine Dragons - Natural.mp4')
        st.text('Natural_Imagine Dragons')
    st.text('')
    st.text('')
    st.text('')
    st.text('Sources: YouTube & Internet')
   

elif choice == 'CamPred':
    st.title('Play fun!')

    cap = cv2.VideoCapture(0)  # device 0

    st.subheader('Take a photo of banknotes, please!')
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
            # st.write('Image is captured:')
            
        captured_image = cv2.resize(captured_image, (224,224))  #Resize Image according to model
        img_array  = np.expand_dims(captured_image, axis=0)     #Resize Image according to model
            # st.write(img_array)                                   #Check the img_array here (no_use this line)
        prediction = model.predict(img_array)
        index = np.argmax(prediction.flatten())

        st.write("Answer: It's", class_names[index], "VND")

elif choice == 'PicPred':
    st.title('Such a rich people!')
    st.image('media/banknotes.png')

    st.subheader('Upload your money')
    photo_uploaded = st.file_uploader('',['png', 'jpeg', 'jpg'])

    if photo_uploaded != None:
        image_np = np.asarray(bytearray(photo_uploaded.read()), dtype=np.uint8)
        img = cv2.imdecode(image_np, 1)
        st.image(img, channels='BGR')
        img_resized = cv2.resize(img, (224,224))                # no_use this line 
        img_array  = np.expand_dims(img_resized, axis=0)        #Expand dim
        prediction = model.predict(img_array)                   #Prediction
        index = np.argmax(prediction.flatten())
        st.write("Answer: It's", class_names[index], "VND")
