# 주어진 정수가 소수인지를 검사하는 함수 testPrime(n)를 작성
# 2부터 100사이의 소수를 출력

def testPrime(n):
    for i in range(2, n+1):
        divisor = 2
        prime = True

        for divisor in range(2, i):
            if i % divisor == 0:
                prime = False
                break
        if i == n:
            if prime == True:
                # print(f"{n}은 소수임")
                return True
            else:
                # print(f"{n}은 소수아님")
                return False

# test_num = int(input("소수인지 확인할 정수를 입력하시오 : "))
# testPrime(test_num)

for i in range(2, 101):
    if testPrime(i):
        print(i, end = ' ')

