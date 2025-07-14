# (x:x*x)형식의 숫자(1과 10 사이)를 key로 포함하는 딕셔너리(comprehesion)을 생성하고 출력하는 프로그램

myList = dict()

# for i in range(1,11):
#     myList[i] = i*i
# print(myList)

# teacher
dic = [ {x:x*x} for x in range(1,11)]
print(dic)