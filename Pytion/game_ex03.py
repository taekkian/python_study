# 요구사항
# 속담의 앞/뒤 부분만 보여주고, 사요자가 맞추는 게임
# 정답은 QR코드로 전달하고, 사용자가 그만둘때까지 게속
import random
import qrcode




try_count = 0
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

try_count = 0
length_proverbs = len(proverbs) # 리스트 개수
# print(length_proverbs)
selected_proverbs = random.sample(proverbs,length_proverbs) # 리스트 순서를 섞는다
for i in range(length_proverbs):
# while True:
    if try_count == 0:
        print("\n다음 속담의 나머지 입력하시오:")
        # print(f"가능한 시도횟수 : {total_try}\n")
        input("준비되면 Enter를 누르세요!")

    # me
    # print("속담 :", front)
    # answer = input("\n입력: ")
    

    
    # teacher
    # front, back = random.choice(proverbs)
    front, back = selected_proverbs[i]
    img = qrcode.make(back)
    img.save(f"testCode{i}.png")
    print(f"정답이 담긴 QR코드가 testCode{i}로 저장되었습니다.")
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

    is_continue = input("그만 하실건가요 (Y) ? : ").strip().lower()
    # try_count += 1
    if is_continue == 'y' or try_count == length_proverbs:
        break
    
# print(f"총 시도횟수중 {try_count} 중 정답횟수는 {score} 입니다.")
print("수고하셨습니다. ")