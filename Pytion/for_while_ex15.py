# 다음 수열의 합을 계산

# teacher
sum = 0
for i in range(1, 100, 2):
    sum += (i/(i+2))
print(sum)