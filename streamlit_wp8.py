
import streamlit as st 
import pandas as pd
import cv2 
import numpy as np 
import matplotlib as plt 
import tensorflow as tf 
import time 

menu = ['Home', 'All about', 'Entertainment', 'PicPred. RICH HOOMAN!', 'CamPred', 'Auto Capture']

choice = st.sidebar.selectbox('MENU', menu)

Model_Path = 'my_model_save.h5'
class_names = ['1000', '10000', '100000', '2000', '20000', '200000', '5000', '50000', '500000']
model = tf.keras.models.load_model(Model_Path)

if choice == 'Home':
    st.header("Welcome to the playground")
    st.text('This is a playground. All about my interests! Leave your signs after visiting!')

    st.image('media/vespa.png', caption = 'Which activity do you like?')
    
    st.text("What's your name?")
    your_name = st.text_input('')
    if your_name != '':
        st.write(your_name,' is a beautiful name!')
        st.write(your_name, "... Let's explore more in the next space. Have fun!")

elif choice == 'Entertainment':
    st.header('FREEDOM YOUR SOUL!')
    st.image('media/Entertainment.png')
    st.subheader('Play your way!')

    st.audio('media/EverythingSucks-Vaultboy.mp3')

    st.video('media/Believer_Imagine Dragons.mp4')
    st.text('Believer _ Imagine Dragons')

   

elif choice == 'CamPred':
    st.title('PLAY FUN!')

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

elif choice == 'Auto Capture':
    TIMER = int(20)
    cap = cv2.VideoCapture(0) # Open the camera
    # run = st.checkbox('Show Webcam')
    
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    
    FRAME_WINDOW = st.image([])
    # while run:
    while True:
            ret, img = cap.read() # Read and display each frame
            cv2.imshow('a', img)

            k = cv2.waitKey(125) # check for the key pressed

            if k == ord('q'): # set the key for the countdown # to begin. Here we set q # if key pressed is q
                prev = time.time()
                while TIMER >= 0:
                    ret, img = cap.read()

                    font = cv2.FONT_HERSHEY_SIMPLEX  # Display countdown on each frame  # specify the font and draw the  # countdown using puttext
                    cv2.putText(img, str(TIMER),
                                (200, 250), font,
                                7, (0, 255, 255),
                                4, cv2.LINE_AA)
                    cv2.imshow('a', img)
                    cv2.waitKey(125)

                    cur = time.time()           # current time
                    if cur-prev >= 1:           # Update and keep track of Countdown  # if time elapsed is one second   # than decrease the counter
                        prev = cur
                        TIMER = TIMER-1
                else:
                    ret, img = cap.read()
                    cv2.imshow('a', img)        # Display the clicked frame for 2 # sec.You can increase time in  # waitKey also
                    cv2.waitKey(2000)           # time for which image displayed
                    cv2.imwrite('camera.jpg', img)  # Save the frame
                    img = cv2.resize(img, (224,224))  #Resize Image according to model
                    img_array  = np.expand_dims(img, axis=0)     #Resize Image according to model
                    prediction = model.predict(img_array)
                    index = np.argmax(prediction.flatten())
                    st.write("Answer: It's", class_names[index], "VND")
                    # HERE we can reset the Countdown timer # if we want more Capture without closing # the camera
            # Press Esc to exit
            elif k == 27:
                break
    cap.release() # close the camera

    #     # close all the opened windows
    # cv2.destroyAllWindows()


elif choice == 'PicPred. RICH HOOMAN!':
    st.title('Such a rich hooman! Prove it!')
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
        st.write('You money is:', class_names[index])
