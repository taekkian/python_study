# 키와 값을 따로 저장하고 있는 2개의 리스트를 써서 하나의 딕셔너리로 만드는 함수 선언

list_a = ['a','b','c','d','e','f','g']
list_b = [1,2,3,4,5,6,7,8]

list_merge = dict()
def merge_and_to_dict(a,b):
    for i in range(min(len(a), len(b))):
        list_merge[a[i]] = b[i]
    return list_merge

print(merge_and_to_dict(list_a,list_b))

