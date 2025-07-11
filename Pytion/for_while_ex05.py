# 중첩 반복문을 사용하여 입력된 정수만큼 *를 순차적으로 출력

num = int(input("정수를 입력하시오 : "))

#  me
for x in range(num):
    print()
    for y in range(x+1):
        print('*', end = ' ')

# teacher
# for i in range(num+1):
#     for j in range(1,num+1):
#         if j <= i:
#             print('*', end = ' ')
#     print()