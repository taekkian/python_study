# 사용자에게 현재 온도를 질문하고 온도가 25이상이면 반바지를 추천하고 25 미만이면 긴바지를 추천

temperature = int(input("현재 온도 "))

if temperature >= 25:
    print("반바지 추천")
else:
    print("긴바지 추천")