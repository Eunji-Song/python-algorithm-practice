"""
상하좌우 좌표 이동
"""
"""
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

