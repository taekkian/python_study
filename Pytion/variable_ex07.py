# 사용자로부터 두 점의 좌표(x1, y1)과 (x2, y2)를 입력받아서 두 점 사이의 거리를 계산
pos_x1 = float(input("x1 좌표를 입력하시오 : "))
pos_y1 = float(input("y1 좌표를 입력하시오 : "))
pos_x2 = float(input("x2 좌표를 입력하시오 : "))
pos_y2 = float(input("y2 좌표를 입력하시오 : "))
distance = ((pos_x1-pos_x2)**2 +(pos_y1-pos_y2)**2)**(1/2)
print("두점 (%.1f,%.1f)과 (%.1f,%.1f) 사이의 거리는 %.2f입니다." %(pos_x1, pos_y1, pos_x2, pos_y2, distance))
