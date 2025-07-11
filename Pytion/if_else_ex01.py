# 사용자로부터 2개의 정수를 받아서 첫번째 저웃가 두번째 정수로 나누어 떨어지는 지 검사
# 약수이면 "약수입니다" 출력
num1 = int(input("첫 번째 정수 입력"))
num2 = int(input("두 번째 정수 입력"))

if num1 % num2 == 0 and num1 != 0 and num2 != 0:
    print("약수 입니다.")
else:
    print("약수가 아닙니다.")