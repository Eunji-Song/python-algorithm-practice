"""
[이것이 코딩테스트다 - 모험가 길드]
한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드신 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오.
"""

# 모험가의 수 > 내림차순
# total = input()
# scaryGuage = sorted(input().split(" "), reverse=True)
# personLen = len(scaryGuage)
# max = int(scaryGuage[0])
# groupLen = 0
#
# while True :
#     if  len(scaryGuage) > max :
#         del scaryGuage[0:max]
#         groupLen += 1
#     else :
#         break;
#
# groupLen += 1



# ---- 답 (오름차순) ----
n = int(input())
data = list(map(int, input().split()))
data.sort() # 입력받은 데이터 오름차순

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data : # 공포도를 낮은 것부터 하나씩 확인
    count += 1 #현재 그룹에 해당 모험가를 포함
    if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result)

