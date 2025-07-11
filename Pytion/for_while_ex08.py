# While을 사용하여 n**2 > 500인 n 중에서 가장 작은 n을 찾는 프로그램

num = 0

# me
# while num**2 <= 500 :
#     num += 1
# print(f"{num}**2 > 500인 최소값은 {num**2} 입니다.")

# teacher 
while num < 500 :
    if (num**2) > 500 :
        print(num)
        break
    num += 1
