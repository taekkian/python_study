# 합, 차, 곱, 나눗셈을 수행하는 함수를 각각 정의한다. 
# 입력값 두 개를 받아서 모든 함수를 한번씩 실행하고 출력

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

num_a = int(input("입력값 a :"))
num_b = int(input("입력값 b :"))

print(f"{num_a}, {num_b} 두수 더하기",add(num_a, num_b))
print(f"{num_a}, {num_b} 두수 빼기",sub(num_a, num_b))
print(f"{num_a}, {num_b} 두수 곱하기",mul(num_a, num_b))
print(f"{num_a}, {num_b} 두수 나누기", div(num_a, num_b))