# 패스워드를 검증하는 함수 checkPass(p)를 정의, 
# 패스워드는 적어도 8글자이상
# 적어도 1글자의 대문자와 소문자, 숫자가 들어가야하고
# 알파벳으로 한정한다.


password = input("패스워드를 입력하시오 : ")

def checkPass(p):
    isUpperStatus = False
    isLowerStatus = False
    isNumericStatus = False
    if len(p) >= 8:
        for letter in p:
            if letter.isupper() == True:
                isUpperStatus = True
            elif letter.islower() == True:
                isLowerStatus = True
            elif letter.isdigit() == True:
                isNumericStatus = True
    if isUpperStatus == True and isLowerStatus == True and isNumericStatus == True:
        print("패스워드 인정")
    else:
        print("패스워드 불인정")

checkPass(password)


    