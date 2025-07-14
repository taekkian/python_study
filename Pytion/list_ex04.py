# 리스트 컴프리핸션을 이용하여 다음과 같이 실행 결과가 출력
# 실행전 [1,2,3,4,5,6,7,8,9,10]
# 실행후 [1,2,-3,-4,-5,-6,-7,-8,9,10]

list_num = [1,2,3,4,5,6,7,8,9,10]

# list_num_2 = [i*-1 for i in list_num]
# teacher 
list_num_2 = [-i if 3 <= i and i <= 8 else i for i in list_num]

print(list_num_2)