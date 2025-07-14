# 달의 번호를 받아서 
# 달의 이름을 출력하는 함수 
# {1:"January", 2:Feburary", 3:"March", 4:"April", 5:"May", 6:"June", 
#  7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

monthDict = {
    1:"January", 2:"Feburary", 3:"March", 4:"April", 5:"May", 6:"June", 
    7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"
    }

number = int(input("1~12 월을 정수로 입력하시오 : "))

def outMonth(monthNum):
    return monthDict.get(monthNum)

print(outMonth(number))


