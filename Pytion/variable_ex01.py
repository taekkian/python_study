# 두개의 정수를 받아서 정수의 합, 차, 곱, 평균, 큰 수, 작은 수를 계산하고 화면에 출력하는 프로그램을 작성
# 내장함수 max(x, y), min(x, y)를 사용
x = int(input("첫 번째? "))
y = int(input("두 번째? "))
sum = x + y
sub = x - y
mul = x * y
avg = sum / 2
num_max = max (x, y)
num_min = min (x, y)

print("수의 합 %d" %sum)
print("수의 차 %d" %sub)
print("수의 곱 %d" %mul)
print("평균 %d" %avg)
print("큰 수 %d" %num_max)
print("작은 수 %d" %num_min)
