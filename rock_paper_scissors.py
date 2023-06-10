import random


choices = ['Rock', 'Paper', 'Scrissors']
computer = random.choice(choices)
player = False
cpu_score = 0 
player_score = 0

while True:
    player = input("Rock, Paper, or Scissors? ").capitalize()
    ## conditions of rock paper scissors
    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You lose! {computer} covers {player}")
            cpu_score+=1
        else:
            print(f"You win! {player} smashes {computer}")
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You lose! {computer} cuts {player}")
            cpu_score+=1
        else:
            print(f"You win! {player} covers {computer}")
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You lose! {computer} smashes {player}")
            cpu_score += 1
        else:
            print(f"You win! {player} cuts {computer}")
            player_score += 1
    elif player == 'End':
        print("Final Scores")
        print(f"Players score: {player_score}")
        print(f"Computer score: {cpu_score}")
        break 