# 사용자가 2개의 정수(a와 b)를 입력하면 이들 정수의 최대 공약수를 찾아라.
# 예를 들어 3과 6의 최대 공약수는 3.

# teacher
num_a = int(input("정수 a : "))
num_b = int(input("정수 b : "))

common = 0 #최대 공약수
max = num_a

if num_a < num_b:
    max = num_b # 두 수중 큰 수를 amx값에 넣는다.
else:
    max = num_a

for i in range(1, max):
    if num_a % i == 0 and num_b % i == 0:
        common = i

print(num_a, "와" , num_b, "최대 공약수는 ", common, "입니다.")