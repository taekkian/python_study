var_x = float(input("실수 입력 : "))

result = 0
if var_x <= 0 :
    result = var_x**2 - 9*var_x + 2
else :
    result = 7*var_x + 2

print(f"입력된 {var_x}에 대한 계산된 함수값은 {result} 이다.")

