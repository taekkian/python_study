# 2번 예제에서 저의한 4개의 함수를 새로운 calc() 함수에서 호출하여
# 두 개의 입력갓을 받아 동시에 수행하고 출력

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

def calc(in_a, in_b):
    print("{num_a}, {num_b} 두수 더하기",add(in_a, in_b))
    print("{num_a}, {num_b} 두수 빼기",sub(in_a, in_b))
    print("{num_a}, {num_b} 두수 곱하기",mul(in_a, in_b))
    print("{num_a}, {num_b} 두수 나누기", div(in_a, in_b))

calc(num_a, num_b)