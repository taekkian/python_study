# 문자열이 저장된 리스트를 만들고
# 문자열 중에서 'aba'처럼 첫번째 문자와 마지막 문자가 동일한 문자열 수를 계산하는 프로그램

string_list = ['aba', 'asdfd', 'dfgsdfsd', 'qerwrr', 'wertw', 'sdfgdfd', 'gdfsg']

equal_count = 0
for string in string_list:
    if string[0] == string[-1]:
        equal_count += 1
        print(f"{string} is {equal_count} .")

print(f"total equal count is {equal_count}")
