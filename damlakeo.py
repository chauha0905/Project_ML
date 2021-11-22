from random import randint
import streamlit as st

menu = ['Rock, paper, scissors']
choice = st.sidebar.selectbox('Homebox', menu)

if choice == 'Rock, paper, scissors':
    player = input("Fill your option: ")
    computer = randint(0,2)
    # Rock, paper, scissors, shoot
    if computer == 0:
        computer = "Rock)"
    if computer == 1:
        computer = "Paper"
    else:
        computer = "Scissors"
    print(computer)

    print("\n---")
    print("You choose: " + player)
    print("Computer chooses: " + str(computer))

    if player == computer:
        print("Draw")
    else:
        if player == "Rock" or player == "rock" or player == "ROCK" or player == "r" or player == "R":
            if computer == "Paper":
                print("Lose")
            else:
                print("Win")
        elif player == "Paper" or player == "P" or player == "paper" or player == "p" or player == "PAPER":
            if computer == "Rock":
                print("Win")
            else:
                print("Lose")
        elif player == "Scissors" or player == "SCISSORS" or player == "S" or player == "s":
            if computer == "Rock":
                print("Lose")
            else:
                print("Win")
        else:
            print("Wrong input! Please retype!")
        
    print("\n---")
