import random
import time

replay = ""
replay_check = ""
wins = 0
loses = 0
ties = 0

def start_playing():

  global replay
  global replay_check
  global wins
  global loses
  global ties
  
  while replay_check != "N":

    while True:
      try:
        user_choice = int(input("Please choose either 1, 2 or 3\n1. Rock\n2. Paper\n3. Scissors\nYour choice: "))
    
        while user_choice > 3 or user_choice < 1:
          time.sleep(1)
          user_choice = int(input("That wasn't a choice! \nPlease choose either 1, 2 or 3\n1. Rock\n2. Paper\n3. Scissors\nYour choice: "))
        break
      except ValueError:
        time.sleep(1)
        user_choice = print("You have to choose a number!")
      
    computer = random.randint(1,3)
    possible_choices = ["Rock", "Paper", "Scissors"]
    player = possible_choices[user_choice-1]
    computer = possible_choices[computer-1]

    print("You have chosen: " + player + "\nThe computer has chosen: " + computer)
    time.sleep(1)

    if player == computer:
      print(f"Both players selected {player}. It's a tie!")
      time.sleep(1)
      replay = input("Would you like to play again? Y or N\n")
      replay_check = replay.upper() 
      ties += 1
      time.sleep(1)

    elif player == "Rock":
      if computer == "Scissors":
        print("Rock beats Scissors! You win!")
        time.sleep(1)
        replay = input("Would you like to play again? Y or N\n")
        replay_check = replay.upper()
        wins += 1
        time.sleep(1)
      else:
        print("Paper beats Rock! You lose.")
        time.sleep(1)
        replay = input("Would you like to play again? Y or N\n")
        replay_check = replay.upper()
        loses += 1
        time.sleep(1)
      
    elif player == "Paper":
      if computer == "Rock":
        print("Paper beats Rock! You win!")
        time.sleep(1)
        replay = input("Would you like to play again? Y or N\n")
        replay_check = replay.upper()
        wins += 1
        time.sleep(1)  
      else:
        print("Scissors beats Paper! You lose.")
        time.sleep(1)
        replay = input("Would you like to play again? Y or N\n")
        replay_check = replay.upper()
        loses += 1
        time.sleep(1)
        
    elif player == "Scissors":
      if computer == "paper":
        print("Scissors beats Paper! You win!")
        time.sleep(1)
        replay = input("Would you like to play again? Y or N\n")
        replay_check = replay.upper()
        wins += 1
        time.sleep(1)
      else:
        print("Rock beats Scissors! You lose.")
        time.sleep(1)
        replay = input("Would you like to play again? Y or N\n")
        replay_check = replay.upper()
        loses += 1
        time.sleep(1)


start_playing()


print("You won {} time(s), Lost {} time(s), and you Tied {} time(s)".format(wins, loses, ties))
