from random import randint
print("Welcome to the game!")
print("if you want to play, you should give me a token")

token =(input("Enter your token: ")) # 토큰을 입력받는다
if token == "token": # 토큰이 token이라면
    print("You have a token, let's make some noise!")
else:  #토큰이 없다면
    print("You don't have a token, you can't play")

while token == "token":#토큰이 있으면 게임을 시작한다
    User_choice = int(input("Enter your choice: "))
    pc_choice = randint(1,100)
    playing = True
    while playing:
        if User_choice == pc_choice:
            print("It's a draw")
            playing = False
        elif User_choice > pc_choice:
            print("You win, Com choose:", pc_choice)
            playing = False
            exit()
        elif User_choice < pc_choice:
            print("You lose, Com choose:", pc_choice)
            playing = False