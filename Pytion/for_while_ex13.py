# 피보니치 수열을 정수 n를 입력 받아 n차까지 출력하는 프로그램

# teacher
num = int(input(" 몇 번째 항까지 구할까요? "))
element1 = 0
element2 = 0

for i in range(num+1):
    if i < 2:
        element2 = element1
        element1 = i
        sum = element1 + element2
    else:
        sum = element1 + element2
        element2 = element1
        element1 = sum
    
    if i != num:
        print(sum, end = ", ")
    else:
        print(sum)