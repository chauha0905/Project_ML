import streamlit as st
import numpy as np

menu = ['Rock, paper, scissors']
choice = st.sidebar.selectbox('Homebox', menu)

if choice == 'Rock, paper, scissors':
    player = st.text_input("Fill your option: ")
    computer = np.random.randint(0,2)
   
    if computer == 0:
        computer = "Rock"
    if computer == 1:
        computer = "Paper"
    else:
        computer = "Scissors"

    st.text("")
    st.write("You choose: ", player)
    st.write("Computer chooses: ", computer)

    if player == computer:
        st.write("Draw")
    else:
        if player == "Rock" or player == "rock" or player == "ROCK" or player == "r" or player == "R":
            if computer == "Paper":
                st.write("You lose!")
            else:
                st.write("You win!")
        elif player == "Paper" or player == "P" or player == "paper" or player == "p" or player == "PAPER":
            if computer == "Rock":
                st.write("You win!")
            else:
                st.write("You lose!")
        elif player == "Scissors" or player == "SCISSORS" or player == "S" or player == "s":
            if computer == "Rock":
                st.write("You lose!")
            else:
                st.write("You win!")
        else:
            st.write("Wrong input! Please retype!")
        
