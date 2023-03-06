stack = []

stack.append(5) #삽입
stack.append(2) #삽입
stack.append(3) #삽입
stack.append(7) #삽입
stack.pop() #마지막에 추가한요소 제거
stack.append(1) #삽입
stack.append(4) #삽입
stack.pop() #마지막에 추가한요소 제거

print(stack[::-1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력