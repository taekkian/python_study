import random

rpc = ['rock', 'paper', 'scissors']
user = input("'rock', 'paper', 'scissors' 중 하나를 입력하시오 : ")

is_wrong  = True
for sel in rpc:
    if sel == user:
        is_wrong = False

if is_wrong == False:
    com = rpc[random.randint(0,2)]

    # 0:바위, 1:보, 2:가위
    print(f"user is {user} and com is {com}")
    if user == com:
        print('draw')
    elif user == 'rock' and com == 'paper':
        print("you lose")
    elif user == 'rock' and com == 'scissors':
        print("You win")
    elif user == 'paper' and com == 'scissors':
        print('You lose')
    elif user == 'paper' and com == 'rock':
        print('You win')
    elif user == 'scissors' and com == 'rock':
        print('You lose')
    elif user == 'scissors' and com == 'paper':
        print('You win')
    else:
        print('wrong')
else:
    print('wrong')
