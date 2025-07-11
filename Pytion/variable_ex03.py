# 삼각형의 두 변의 길이를 받아서 나머지 변의 최대 길이를 계산
tri_side_a = int(input("삼각형 첫 번째 변? "))
tri_side_b = int(input("삼각형 두 번째 변? "))
max_side = tri_side_a + tri_side_b -1
print("삼각형의 나머지 변의 최대 길이는 %d입니다." %max_side)
