"""
# 그리디 알고리즘
* 거스름돈 문제
1. 큰 단위부터 나눈다 -> 큰 단위가 작은단위의 배수인 경우
2. 큰 단위가 작은 단위의 배수가 아닌 경우 이 그리디 알고리즘을 사용하는것이 올바른지 확인해봐야함.
"""

n = 1260
count = 0

# 큰 단위부터 확인
array = [500, 100, 50, 10]
for coin in array :
    count += n // coin # 동전의 개수 세기
    n %= coin
print("cnt " ,  count)