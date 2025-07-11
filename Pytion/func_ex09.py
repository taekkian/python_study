# 사용자로부터 2개의 정수를 입력받아서 최대 공약수를 찾는 함수
num_a = int(input("정수 a : "))
num_b = int(input("정수 b : "))

def gcd_calculator(a, b):
    common = 0 #최대 공약수
    max = a

    if a < b:
        max = b # 두 수중 큰 수를 amx값에 넣는다.
    else:
        max = a

    for i in range(1, max):
        if a % i == 0 and b % i == 0:
            common = i
    return common

cal_common = gcd_calculator(num_a, num_a)
print(num_a, "와" , num_b, "최대 공약수는 ",cal_common, "입니다.")