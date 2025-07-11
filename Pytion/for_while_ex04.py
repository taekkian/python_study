# 사용자가 입력한 정수의 모든 약수를 화면에 출력하는 프로그램.

num = int(input("정수를 입력하시오 : "))

for x in range(1, num+1):
    if num % x == 0:
        print(x, end = " ")
