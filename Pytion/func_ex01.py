# 원의 둘레를 계산하는 함수 get_peri(radius)을 정의하고
# radius의 초기값을 5로 정의한다

# me
def get_peri(radius = 5):
    print(2 * 3.14 * radius)

get_peri()
get_peri(10)

# teacher
# from math import pi
# def get_peri(radius = 5.0):
#     circle = 2*pi*radius
#     return circle

# print("get_peri() = ", get_peri())
# print("get_peri(4.0) = ", get_peri(4.0))

# input 추가