
import streamlit as st 
import pandas as pd
import cv2
import numpy as np 
import matplotlib as plt 
import tensorflow as tf 
import random

st.set_page_config(layout='centered', initial_sidebar_state='auto')

# Add prediction model _ VND Banknotes
# Model_Path = 'my_model_save.h5'
Model_Path = 'model.h5'
class_names = ['1000', '10000', '100000', '2000', '20000', '200000', '5000', '50000', '500000']
model = tf.keras.models.load_model(Model_Path)

# Layout the streamlit app
menu = ['The playground', 'Childhood game', 'PicPred', 'CamPred', 'Entertainment']
choice = st.sidebar.selectbox('Homebox', menu)

with st.sidebar:
    st.text('') 
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('') 
    st.image('media/Playground.gif')

    # Add in date & time in sidebar
    st.date_input('Today')
    st.time_input('Current time')

# Start decor and build content
if choice == 'The playground':
    st.title("T h e p l a y g r o u n d")
    st.text('Leave your signs after visiting!')
    st.text('')
    st.image('media/2.png')
    st.subheader('Hi there.')

    wishes = ["Have a good day!", "Enjoy your day!", "Such a beautiful day. Enjoy it!", "It's a good day for going out. Meet your friends!"]    
    
    col1, col2 = st.columns(2)
    with col1:
        your_name = st.text_input("What's your name?")
    with col2:
        gender = st.text_input('Are you male? (y/n)')
    
    if your_name != '':
        if gender == 'y' or gender == 'Y':
            st.write(your_name, " is a great name.")
            st.write(random.choice(wishes))
        elif gender == 'n' or gender == 'N':
            st.write(your_name, " is a lovely name.")
            st.write(random.choice(wishes))

elif choice == 'Childhood game':
    st.title('The priceless treasure.')
    st.text("What was your childhood's memory?")
    st.image('media/game3.png')
    st.header('Rock. Paper. Scissors. SHOOT!')
    
    col1, col2 = st.columns([1, 1.1])
    with col1:
        st.text("This is a game named 'đấm-lá-kéo'.")
        st.text("Tips: Enter your choice by words:")
        st.text("* Rock/rock/ROCK/r/R")
        st.text("* Paper/paper/PAPER/p/P")
        st.text("* Scissors/scissors/SCISSORS/s/S")
    # Game content
    with col2:
        player = st.text_input('Fill your choice & Enter')
        computer = np.random.randint(0,3)
    
        if computer == 0:
            computer = "Rock"
        elif computer == 1:
            computer = "Paper"
        else:
            computer = "Scissors"

        st.text("")
        st.write("You choose: ", player)
        st.write("The childhood chooses: ", computer)

        if computer == player:
            st.write("Draw")
        else:
            if player == 'Rock' or player == 'ROCK' or player == 'rock' or player == 'r' or player == 'R':
                if computer == "Paper":
                    st.write("You lose!")
                else:
                    st.write("You won!")
            elif player == "Paper" or player == 'PAPER' or player == "paper" or player == "p" or player == "P":
                if computer == "Rock":
                    st.write("You won!")
                else:
                    st.write("You lose!")
            elif player == "Scissors" or player == "SCISSORS" or player == "scissors" or player == "s" or player == 'S':
                if computer == "Rock":
                    st.write("You lose!")
                else:
                    st.write("You won!")
            else:
                st.write("WRONG INPUT! Please redo!")

elif choice == 'Entertainment':
    st.title('Enjoy your way!')
    col1, col2 = st.columns(2)
    with col1:
        st.image('media/Thumb2.gif')
    with col2:
        st.text('')
        st.audio('media/Perfect - Ed Sheeran.mp3')
        st.text('Perfect _ Ed Sheeran')
        st.text('')
        st.audio('media/Always Remember Us This Way-Lady Gaga.mp3')
        st.text('Always remember us this way _ Lady Gaga')
        st.audio('media/EverythingSucks-Vaultboy.mp3')
        st.text('Everything sucks _ Vaultboy')
        st.text('')
        
    col1, col2 = st.columns(2)
    with col1:
        video_file = open('media/Believer - Cover.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.text('Believer_Cover by Kids')
    with col2:
        st.video('media/Imagine Dragons - Natural.mp4')
        st.text('Natural_Imagine Dragons')
    st.text('')
    st.text('(Sources: YouTube & Internet)')
   
elif choice == 'CamPred':
    st.title('Play fun!')

    cap = cv2.VideoCapture(0)  # device 0
    st.subheader('Take a photo of banknotes, please!')
    st.text('(Using Vietnamese dong only)')
    run = st.checkbox('Show Webcam')
    capture_button = st.checkbox('Capture') 	

    captured_image = np.array(None)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    FRAME_WINDOW = st.image([])
    while run:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)        
        # Display Webcam
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)          #Convert color
        FRAME_WINDOW.image(frame)

        if capture_button:      
            captured_image = frame
            break

    cap.release()
    # Processing & Prediction
    if  captured_image.all() != None:
        captured_image = cv2.resize(captured_image, (224,224))  #Resize Image according to model
        img_array  = np.expand_dims(captured_image, axis=0)     #Expand dim
        prediction = model.predict(img_array)                   #Prediction by array
        index = np.argmax(prediction.flatten())                 
        st.write("Answer: It's", class_names[index], "VND")
        st.write("The predictions can work not well sometimes. Don't be serious.")
        st.write('JUST FOR FUN!')

    st.success('Application status: In progress')

elif choice == 'PicPred':
    st.title('Such a rich people!')
    st.image('media/Thumb3.png')
    st.text("")
    st.subheader('Upload your money')
    st.text('(Using Vietnamese dong only)')

    photo_uploaded = st.file_uploader('',['png', 'jpeg', 'jpg'])
    # Processing image & prediction
    if photo_uploaded != None:
        image_np = np.asarray(bytearray(photo_uploaded.read()), dtype=np.uint8)
        img = cv2.imdecode(image_np, 1)
        st.image(img, channels='BGR')
        img_resized = cv2.resize(img, (224,224))                #Resize Image according to model
        img_array  = np.expand_dims(img_resized, axis=0)        #Expand dim
        prediction = model.predict(img_array)                   #Prediction
        index = np.argmax(prediction.flatten())
        st.write("Answer: It's", class_names[index], "VND")
        st.write("The predictions can work not well sometimes. Don't be serious.")
        st.write('JUST FOR FUN!')
    
# Thank you!