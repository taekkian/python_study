# 다음리스트에 저장된 정수들의 합을 계산하는 프로그램.
# sum() 사용하지 말고 작성.
myList = [11, 22, 23, 99, 81, 93, 35]

sum = 0
for num in myList:
    sum = sum + num

print(f"List {myList}의 합은 {sum}")