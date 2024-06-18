from random import randint

User_choice = int(input("Enter your choice: "))
pc_choice = randint(1,100)
playing = True
while playing:
    if User_choice == pc_choice:
        print("It's a draw")
    elif User_choice > pc_choice:
        print("You win, com choose:", pc_choice)
        playing = False
    elif User_choice < pc_choice:
        print("You lose, com choose:", pc_choice)