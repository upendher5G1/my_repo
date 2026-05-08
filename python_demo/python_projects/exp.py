import random
choices = ["rock", "paper", "scissors"]
print("/---ROCK,PAPER & SCISSORS GAME---/")
while True:
    computer = random.choice(choices)
    user = input("Enter rock, paper, or scissors: ").lower()
    if user == "exit":
        print("Thank You For Playing!")
        break
    print("Computer chose:", computer)
    if user == computer:
       print("It's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You Won")
    elif user == "paper" and computer == "rock":
        print("You Won")
    elif user == "scissors" and computer == "paper":
        print("You Won")
    else:
        print("Computer wins!")
    