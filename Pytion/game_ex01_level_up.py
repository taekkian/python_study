# 오타가 없을 때까지 입력을 받도록 수정.
# 정확도 대신, 오타 횟수 출력

import random
import time

stringList = ["다 된 죽에 코 풀기",
              "닭 잡아먹고 오리발 내민다",
              "떼어 놓은 당상",
              "뛰는 놈 위에 나는 놈 있다",
              "백문이 불여일견",
              "불난 집에 부채질한다",
              "사촌이 땅을 사면 배가 아프다",
              "다리 긁는 개도 배 아프다",
              "열 길 물속은 알아도 한 길 사람 속은 모른다",
              "똥 묻은 개가 겨 묻은 개 나무란다"]

# sel_string = random.choice(stringList)
# print(sel_string)

# start_time = time.time()
# user_string = input("문장을 따라쓰세요 \n:")
# end_time = time.time()
# check_time = end_time - start_time
# print(f"소모된 시간은 {check_time:.2f} 입니다.")

# # me
# # 타이핑된 문자가 적으면 에러남 teacher pick
# # i = 0
# # right_cnt = 0
# # for letter in sel_string:
# #     if letter == user_string[i]:
# #         right_cnt += 1
# #     i += 1


# # teacher
# right_cnt = 0
# for i in range(min(len(sel_string), len(user_string))):
#     if sel_string[i] == user_string[i]:
#         right_cnt += 1


# # print(len(sel_string))
# # print(right_cnt)

# accuracy = right_cnt/len(sel_string) * 100

# print(f"문장 타이핑의 정확도는 {accuracy:.2f}%입니다.")

# teacher
target = random.choice(stringList)
print("\n다음 문장을 그대로 입력하시오:\n")

def typing_game(target):
    print(f"{target}\n")
    input("준비되면 Enter를 누르세요!")

    # 시간 측정 시작
    start_time = time.time()

    # 사용자 입력 받기
    typed = input("\n입력: ")

    # 시간 측정 종료
    end_time = time.time()
    elapsed = end_time - start_time

    # 정확도 개선
    correct = 0
    for i in range(min(len(target), len(typed))):
        if target[i] == typed[i]:
            correct += 1

    # accuracy = correct / len(target) * 100
    accuracy = correct / max(len(target),len(typed)) * 100

    return accuracy

try_count = 0
is_continue = True

while is_continue == True:
    typing_accuray= typing_game(target)
    if typing_accuray == 100:
            is_continue = False
    else:
         try_count += 1

print(f"문장 타이핑의 오타시도는 {try_count}회 입니다.")

        

