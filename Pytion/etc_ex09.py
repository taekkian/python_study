# 2개의 문자열을 받아서 
# 이들 문자열에  모두 포함된 글자를 출력하는 함수 선언
stringA = input("첫 번째 문자열을 입력 : ")
stringB = input("두 번째 문자열을 입력 : ")

def interString(a,b):
    x = set(a)
    y = set(b)
    return x & y

outString = sorted(interString(stringA, stringB))
print(str(outString))