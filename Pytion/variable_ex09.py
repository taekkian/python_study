number = int(input("4자리 정수를 입력하시오 : "))
input_number = number
x1 = number // 1000
number = number % 1000
x2 = number // 100
number = number % 100
x3 = number // 10
x4 = number % 10
sum_x = x1 + x2 + x3 + x4
print("%d 자리수의 총합은 %d 입니다." %(input_number, sum_x))