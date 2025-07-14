# 리스트에 저장된 값으로 다음과 같이 별표를 출력

num_list = [4,5,6,7,8,9,10]

for i in range(len(num_list)):
    print(f"{num_list[i]} :",'*'*num_list[i])
