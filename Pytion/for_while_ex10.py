# 1**2 + 2**2 + 3**2 + 4**2 +... n**2 의 값을 계산하여 출력

num = int(input("정수를 입력하시오 : "))

sum = 0
for x in range(1, num+1):
    sum = sum + x**2

print(f"계산값은 {sum} 이다.")
