from random import randint
import streamlit as st

menu = ['Rock, paper, scissors']
choice = st.sidebar.selectbox('Homebox', menu)

if choice == 'Rock, paper, scissors':
    player = st.text_input("Fill your option: ")
    computer = randint(0,2)
    # Rock, paper, scissors, shoot
    if computer == 0:
        computer = "Rock)"
    if computer == 1:
        computer = "Paper"
    else:
        computer = "Scissors"
    st.write(computer)

    st.text("\n---")
    st.write("You choose: " + player)
    st.write("Computer chooses: " + str(computer))

    if player == computer:
        st.write("Draw")
    else:
        if player == "Rock" or player == "rock" or player == "ROCK" or player == "r" or player == "R":
            if computer == "Paper":
                st.write("Lose")
            else:
                st.write("Win")
        elif player == "Paper" or player == "P" or player == "paper" or player == "p" or player == "PAPER":
            if computer == "Rock":
                st.write("Win")
            else:
                st.write("Lose")
        elif player == "Scissors" or player == "SCISSORS" or player == "S" or player == "s":
            if computer == "Rock":
                st.write("Lose")
            else:
                st.write("Win")
        else:
            st.write("Wrong input! Please retype!")
        
