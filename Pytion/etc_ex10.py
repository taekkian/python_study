# set1, set2 2개의 세트가 아래와 같고 
# 두 set중 어느 한쪽에만 있는 요소를 출력하는 함수 선언
# set1 = {x*10 for x in range(1,7)} 
# set2 = {x*10 for x in range(3,9)}

set1 = set()
set2 = set()
set1 = {x*10 for x in range(1,7)}
set2 = {x*10 for x in range(3,9)}

def inSet(a,b):
    c = a & b
    d = (a - c) | (b - c)
    return d

outSet = inSet(set1, set2)
print(f"{set1}과 {set2}에서 한쪽에만 있는 요소의 집합은 {outSet}이다")