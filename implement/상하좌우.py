"""
상하좌우 좌표 이동
여행가 A는 N * N 크기의 정사각형 공간 위에 서있다. 이공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른 쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상, 하 ,좌 ,우 방향으로 이동할 수 있으며
시작좌표는 항상(1, 1)이다. 우리앞에는 여행가가 A가 이동할 계획서가 놓여있다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D중 하나의 문자가 반복적으로 적혀 있다. 각 문자의 의미는
다음과 같다.

L : 왼쪽으로 한 칸 이동
R : 오른쪽으로 한 칸 이동
U : 위로 한 칸 이동
D : 아래로 한 칸 이동
이때 여행가 A가 N × N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다

"""

"""
# 내가 쓴 답변 
n = int(input())
step = list(map(str, input().split(" ")))
nowPosX = 0;
nowPosY = 0;
nowPos = {'x':0,'y':0}


for i in step :
    if (i == 'R') :
        print("right")
        if (nowPosX + 1 <= n) :
            nowPosX += 1
    elif i == 'L' :
        print("left")
        if (nowPosX - 1 >= 0) :
            nowPosX -= 1
    elif i == 'U' :
        print("up")
        if (nowPosY - 1 >= 0) :
            nowPosY -= 1
    elif i == 'D' :
        print("down")
        nowPosY += 1
        if (nowPosY + 1 <= n) :
            nowPosY += 1
    nowPos['x'] = nowPosX;
    nowPos['y'] = nowPosY;

print(nowPos)

"""
# 답안 풀이
n = int(input())
x,y = 1, 1
plans = input().split()

# 이동방향
move_types = ["L","R","U","D"]

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동 계획을 확인하기
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간 범위 확인
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue

    # 이동
    x,y = nx, ny

print(x,y)

