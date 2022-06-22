import random

rock = 0
paper = 1 
scissors = 2

computer_won = 0
user_won = 0

# computer_choice = random.randint(0,2)

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# rock > scissors
# scissors > paper
# paper > rock

while True:
    user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors... enter 42 to quit: "))
    computer_choice = random.randint(0,2)

    if computer_choice == rock and user_choice == scissors:
        computer_won += 1
        print ("Computer chose Rock, you lost")
    elif user_choice == rock and computer_choice == scissors:
        user_won += 1
        print ("Rock beats scissors, nice ONE!")
    if computer_choice == scissors and user_choice == paper:
        computer_won += 1
        print ("Snip Snip -> you lost")
    elif user_choice == scissors and computer_choice == paper:
        user_won += 1
        print ("you chose scissors, and computer chose paper, you WIN!")

    if computer_choice == paper and user_choice == rock:
        computer_won += 1
        print ("Computer chose paper, and you chose rock, you lost :(")
    elif user_choice == paper and computer_choice == rock:
        user_won += 1
        print ("You chose paper, and computer chose rock, you WON")

    if computer_choice == user_choice:
        print("You tied")
    if user_choice == 42:
        break
    

print ("Thanks for playing :) ")
print (f"Computer won {computer_won} time and user won {user_won} times")

if computer_won > user_won:
    print(":(")
else:
    print (":)")