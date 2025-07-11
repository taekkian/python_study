# 사용자로부터 3개의 정수를 받아서 수학 문제를 만들어서 출력하는 함숭를 정의

import random
num_a = int(input("첫번째 정수 입력 : "))
num_b = int(input("두번째 정수 입력 : "))

def acc_func(a, b):
    acc_list = ['+', '-', '*', '/']
    sel_acc = acc_list[random.randint(0,3)]

    match sel_acc:
        case '+':
            cal_number = a + b
        case '-':
            cal_number = a - b
        case '*':
            cal_number = a * b
        case '/':
            cal_number = round(a / b, 2)
    
    print(f"{a} {sel_acc} {b} = {cal_number} 입니다.")

acc_func(num_a, num_b)
