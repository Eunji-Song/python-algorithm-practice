
"""
어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행
단, 두번째 연산은 N이 K로 나누어떨어질 때만 선택 할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성하시오.
"""

# 두 수 입력받기
n, k = map(int, input().split())

result = 0

while True :
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    #N이 K보다 작을 때 ( 더 이상 나눌 수 없을 때 )
    if n < k :
        break

    #K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n -1)
