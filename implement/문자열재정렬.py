"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오른차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
ex) K1KA5CB7 -> ABCKK13
"""
"""
# ---- 내가 작성한 코드 ----
# 문자열 입력 받기
str = input()
str_list = [];
sum = 0;

for i in range(len(str)) :
    if str[i].isdigit() == True :
        sum += int(str[i])
    else :
        str_list.append(str[i])

str_list.sort()
result = "".join(str_list) + "{}".format(sum)

print(result)
"""


# ---- 답안 코드 ----
data = input()
result = []
value = 0

# 알파벱, 숫자 검사 후 분리
for x in data :
    if x.isalpha() :
        result.append(x)
    else :
        value += int(x)

result.sort() # 오름차순 정렬

if value != 0 :
    result.append(str(value))

print("".join(result))

