# 사용자로부터 키를 입력받고 표준 체중을 계산. 
# if-else를 사용하여 저체중, 표준, 과체중을 출력

height = int(input("키를 입력하시오 : "))
weight = int(input("몸무게를 입력하시오 : "))

standard_weight = (height-100)*0.9

print(f"키에 대한 표준체중은 {standard_weight} 입니다.")
print("당신은 ")

if weight > standard_weight:
    print("과체중")
elif weight < standard_weight:
    print("저체중")
else:
    print("표준체중")