# 너가 이 속담을 알아?

# 요구 사항
#  속담의 앞/뒤 부분만 보여주고 사요자가 맞추는 게임
#  예) 가는 말이 고와야 ____ 오는 말이 곱다.
# 게임은 5회 진행되고, 이후 맞춘 개수를 출력

# level up
# 오답을 입력했을때, 정답의 일부(ex, 첫글자)를 힌트로 보여주는 기능 추가
# 힌트를 보고, 한번 더 입력하다록 기능 추가



import random

# 총 시도횟수
total_try = 10
score = 0

proverbs = [
    ["다 된 죽에", "코 풀기"],
    ["닭 잡아먹고", "오리발 내민다"],
    ["떼어 놓은", "당상"],
    ["뛰는 놈 위에", "나는 놈 있다"],
    ["아니 땐 굴뚝에", "연기 나랴"],
    ["불난 집에", "부채질한다"],
    ["사촌이 땅을 사면", "배가 아프다"],
    ["다리 긁는 개도", "배 아프다"],
    ["열 길 물속은 알아도", "한 길 사람 속은 모른다"],
    ["똥 묻은 개가", "겨 묻은 개 나무란다"]
]

def answer_string(score_inc):
    print("정답입니다.\n")
    score_inc += 1
    return score_inc

# for 문 사용
#반복된 사용을 방지 random.sample 사용
selected_proverbs = random.sample(proverbs,total_try) 
for i in range(total_try):
    if i == 0:
        print("\n다음 속담의 나머지 입력하시오:")
        print(f"가능한 시도횟수 : {total_try}\n")
        input("준비되면 Enter를 누르세요!")

    # me
    # print("속담 :", front)
    # answer = input("\n입력: ")
    

    
    # teacher
    # front, back = random.choice(proverbs)
    front, back = selected_proverbs[i]
    print(f"속담 : \"{front}", '_' * len(back), "\"")
    answer = input("뒷부분을 입력하세요: ").strip()
    if back == answer :
        score = answer_string(score)
    else:
        hint = back[0] # 첫 글자
        length = len(back) 
        print(f"오답입니다 첫글자 힌트는 \"{hint}\"입니다. 길이는 {length} 입니다.")
        answer = input("첫글자를 포함한 뒷부분을 입력하세요: ").strip()
        if back == answer :
           score = answer_string(score)
        else:
            print(f"오답입니다 정답은 \"{back}\"입니다.\n")

# while 문 사용
# i = 0
# while True:
#     if i == 0:
#         print("\n다음 속담의 나머지 입력하시오:")
#         print(f"가능한 시도횟수 : {total_try}\n")
#         input("준비되면 Enter를 누르세요!")

#     # me
#     # print("속담 :", front)
#     # answer = input("\n입력: ")
    

    
#     # teacher
#     front, back = random.choice(proverbs)
#     print(f"속담 : \"{front}", '_' * len(back), "\"", f": {len(back)}글자")
#     answer = input("뒷부분을 입력하세요: ").strip()
#     you_try = i + 1
#     if back == answer :
#         print("정답입니다.")
#         print()
#         score += 1
#     else:
#         print("오답입니다")
#         print()
#     i += 1
#     if i == 5:
#         break

print(f"총 시도횟수 {total_try} 중 정답횟수는 {score} 입니다.")


