# 사용자로부터 정수 리스트를 받아서 
# 리스트에 있는 중보된 요소들을 제거하고 리스트를 정렬시키는 프로그램

my_list = list()
for i in range(5):
    my_list.append(int(input("임의의 정수를 입력하시오 :  ")))

list_2 = set(my_list)
list_2 = list(list_2)
list_2.sort()

print(list_2)