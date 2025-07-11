# 성적이 90점이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 그외에는 F를 반확하는 함수

def cal_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

num = int(input("점수를 입력하시오 : "))

print(f"당신의 성적은 {cal_grade(num)}입니다.")