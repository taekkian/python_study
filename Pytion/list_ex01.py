# 입력받을 수를 입력받고 
# 리스트로 그 수만큼 다시 입력을 저장하고 
# 합계를 계산하는 프로그램


length_list = int(input("정수를 입력하시오 (리스트 개수) :"))

num_list = []
sum_num = 0
for i in range(length_list):
    number = int(input("리스트에 넣을 정수를 입력하시오 : "))
    num_list.append(number)
    sum_num += num_list[i]

print(f"{num_list}의 총합은 {sum_num}입니다")


