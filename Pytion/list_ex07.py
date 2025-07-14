import random 

# 다음과 같은 리스트를 생성하고 무작위로 항목을 선택하는 프로그램
# myList = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']

myList = []
for i in range(10):
    myList.append(f'a{i}')

print(myList)
random_count = random.randint(1,len(myList))
