# 2개의 리스트를 받아서 
# 공통 구성원이 하나 이상 있으면 True를 반환하는 함수를 작성.

list_a = [1,2,3,4,5,6]
list_b = [5,6,7,8,9,10]

def single_list(alist):
    aset = set(alist)
    non_same = list(aset)
    return non_same

def same_element(a,b):
    same_list = [i for i in a for j in b if i == j]
    only = single_list(same_list)
    print('결과', only)

same_element(list_a, list_b)