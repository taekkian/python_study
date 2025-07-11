# 윈의 넓이를 계산하는 프로그램을 만들고 사용자가 입력한 원의 반지름으로 계산해서 출력
# 음수 입력의 경울 "잘못된 값입니다."
radius = float(input("원의 반지름을 입력하시오"))

if radius < 0:
    print("잘못된 입력값입니다.")
else:
    area = 3.14*radius**2
    print(f"입력된 반지름 {radius}의 넓이는 {area}입니다.")
