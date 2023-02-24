"""
[이것이 코딩테스트다 - 곱하기혹은더하기]
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램.
단, + 보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어짐

예를들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 (((((0+2)*9)*8)*4) = 576
만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수
"""


# ============== 내가 작성한 코드 ==============
value = input()
numList = list(value)
sum = 0;

for idx, num  in enumerate(numList) :
    num = int(num)

    if (num <= 1 or sum <= 1) :
        sum += num
    else :
        sum *= num

print("sum : ", sum)


# ==============  답안 코드  ==============
data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)) :
    # 두 수 중에서 하나라도 0 혹은 1인 경우 곱하기 보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += sum
    else :
        result *= sum

print(result)
