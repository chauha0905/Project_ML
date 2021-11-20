import streamlit as st
import pandas as pd
import cv2
import numpy as np 
import matplotlib as plt 
import tensorflow as tf 

menu = ['Home', 'All about', 'Projects', 'Share your image', 'Music', 'Videos', 'CamPred. PLAY FUN!']

choice = st.sidebar.selectbox('MENU', menu)

if choice == 'Home':

    st.header("Welcome to the playground")
    st.text('This is a playground. All about my interests! Leave your signs after visiting!')

    st.image('media/vespa.png', caption= 'Which activity do you like?')
    
    your_name = st.text_input("What's your name?")
    if your_name != '':
        st.write(your_name,' is a beautiful name!')
        st.write(your_name, ", let's explore more in the next space. Have fun!")


elif  choice == 'Share your image':
    st.title('Open your webcam')
    st.warning('Webcam shows on local computer ONLY!')
    show = st.checkbox('Show!')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while show:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        camera.release()

elif choice == 'CamPred. PLAY FUN!':
    Model_Path = 'my_model_save.h5'
    class_names = ['1000', '2000', '5000', '10000', '20000', '50000', '100000', '200000', '500000']
    model = tf.keras.models.load_model(Model_Path)

    cap = cv2.VideoCapture(0)
    run = st.checkbox('Show Webcam')
    capture_button = st.checkbox('Capture')

    captured_image = np.array(None)

    if not cap.isOpened():
        FRAME_WINDOW = st.image([])
        while run:
            ret, frame = cap.read()        
            # Display Webcam
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB ) #Convert color
            FRAME_WINDOW.image(frame)

            if capture_button:
                captured_image = frame 
                break
        cap.release()

        if captured_image.all() != None:
            st.image(captured_image)
            st.write('Image is captured: ')

            #Resize the Image according with your model
            captured_image = cv2.resize(224)
            #Expand dim to make sure your img_array is (1, Height, Width , Channel ) before plugging into the model
            img_array  = np.expand_dims(captured_image, axis=0)
            #Check the img_array here
            st.write(img_array)

            prediction = model.predict(img_array)



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