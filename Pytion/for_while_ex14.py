# 2와 20 사이에 있는 모든 소수를 찾는 프로그램.
# (예제 7은 소수, 자신과 1만이 약수) 나누었을때 목이 0


# teacher

maxNum = 20
number = 2
count = 0

# while  number < maxNum:
#     divisor = 2
#     prime = True

#     while divisor < number:
#         if number % divisor  == 0:
#             prime = False
#             break
#         divisor += 1
#     if prime == True:
#         count += 1
#         print(number, end = " ")
#     number += 1


# for

# me
# for x in range(number, maxNum):
#     prime = True
#     for y in range(2, x):
#         if x % y == 0:
#             prime = False
#             break
#     if prime == True:
#         count += 1
#         print(x, end = ' ')

# teacher

# for i in range(2, maxNum+1):
#     divisor = 2
#     prime = True


#     for divisor in range(2, number):
#         if number % divisor == 0:
#             prime = False
#             break
#     if prime == True:
#         count += 1
#         print(number, end = " ")
#     number += 1

for i in range(2, maxNum+1):
    divisor = 2
    prime = True

    for divisor in range(2, i):
        if i % divisor == 0:
            prime = False
            break
    if prime == True:
        count += 1
        print(i, end = " ")


