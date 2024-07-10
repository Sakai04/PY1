from random import randint #라이브러리 호출

User_choice = int(input("Enter your choice: "))
pc_choice = randint(1,100)

if User_choice == pc_choice:#if 문
    print("It's a draw")
elif User_choice > pc_choice:
    print("You win, com choose:", pc_choice)
elif User_choice < pc_choice:
    print("You lose, com choose:", pc_choice)
    