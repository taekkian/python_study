# 사용자로부터 1000000 에서 999999사이의 숫자를 읽어서 천단위를 구분하는 쉼표를 넣어서 화면에 출력
input_number = int(input("100000에서 999999사이의 숫자를 입력하시오 "))

if input_number >= 100000 and input_number <= 999999 :
    comma_digit1 = input_number // 1000
    comma_digit2 = input_number % 1000
    print(comma_digit1,",",comma_digit2)
    print(str(comma_digit1)+","+str(comma_digit2))
    print("%d 숫자는 %d,%d와 동일하다" %(input_number, comma_digit1, comma_digit2))
    print(f"{input_number} 숫자는 {input_number:,}와 동일하다. @")
else:
    print("슷자가 입력된 범위에 없습니다.")