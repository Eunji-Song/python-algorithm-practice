"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
모든 경우의 수를 구하는 프로그램을 작성하세요. 
"""

h = int(input())
count = 0

for i in range(h + 1) : #hour
    for m in range(60) : #minute
        for s in range(60) : #second
            if '3' in str(i) + str(m) + str(s) :
                count += 1


print(count)
