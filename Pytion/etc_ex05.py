# 딕셔너리에 쇼핑몰에서 구입한 상품의 가격이 저장되어 있다. 딕셔너리에 있는 모든 상품의 가격의 합계를 계산하는 함수를 선언
# my_dic = {"옷":100, "컴퓨터":2000, "모니터":320}


my_dic = {"옷":100, "컴퓨터":2000, "모니터":320}

# my_dic.values
sum = 0

for value in my_dic.values():
    sum += value

print(sum)