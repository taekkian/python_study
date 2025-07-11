# 덧셈, 뺄셈, 곱셈, 나줏셈 중 하나를 랜덤으로 선택하고
# 두 정수값을 랜덤으로 생성하여 
# 문제를 만들어 사용자로부터 답을 입력받아 정답 혹은 오답을 판단하는 프로그램
# if-else와 random.randint를 사용

import random

acc_list = ['+', '-', '*', '/']
sel_acc = acc_list[random.randint(0,3)]
# sel_acc = '/'

random_number1 = random.randint(1,9)
random_number2 = random.randint(1,9)

print(f"선택된 산술은 \'{sel_acc}\' 입니다.")
print(f"생선된 두 정수는 {random_number1}, {random_number2}입니다.")
print(f"{random_number1} {sel_acc} {random_number2} 의 값울 넣으세요")

if sel_acc == '/' :
    print("소수점 세째 자리까지 버림")
    your_number = float(input("계산된 실수를 입력하시요 : "))
    your_number = round(your_number,2)
else:
    your_number = int(input("계산된 정수를 입력하시요 : "))

cal_number = 0

# if sel_acc == '+':
#     cal_number = random_number1 + random_number2
# elif sel_acc == '-':
#     cal_number = random_number1 - random_number2
# elif sel_acc == '*':
#     cal_number = random_number1 * random_number2
# elif sel_acc == '/':
#     cal_number = round(random_number1 / random_number2, 2)

match sel_acc:
    case '+':
        cal_number = random_number1 + random_number2
    case '-':
        cal_number = random_number1 - random_number2
    case '*':
        cal_number = random_number1 * random_number2
    case '/':
        cal_number = round(random_number1 / random_number2, 2)    

if cal_number == your_number:
    print("정답")
else:
    print("오답")