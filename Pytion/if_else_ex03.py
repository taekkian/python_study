# 사용자로부터 하나의 문자를 입력받고 문자가 
# 'R'이나 'r'이면 Rectangle이라고 출력,
# 'T'나 't'이면 Triangle이라고 출력,
# 'C'나 'c'이면 Circle이라고 출력,
# 그외에 문자가 들어오면 Unknown이라고 출력

one_char = input("하나의 문자 입력")

if one_char == 'R' or one_char == 'r':
    print("Rectangle")
elif one_char == 'T' or one_char == 't':
    print("Triangle")
elif one_char == 'C' or one_char == 'c':
    print("Circle")
else:
    print("Unknown")