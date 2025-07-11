# 사용자가 일정 구간의 값을 입력할때까지 사용자가 입력을 요청하는 함수 getIntRange(a, b, msg)를 작성하고
# 날짜(월,일)를 입력받아서 출력

def getIntRange(a,b,msg):
    is_continue = True
    while is_continue:
        input_number = int(input(msg))
        if input_number >= a and input_number <= b:
            is_continue = False
    return input_number


month = getIntRange(1,12,"월을 입력하시오(1부터 12사이의 값) : ")
day = getIntRange(1,31,"월을 입력하시오(1부터 31사이의 값) : ")

print(f"{month}월 {day}일")

