# 1주차 20201031 문제 분석 및 알고리즘 순서도 작성: 완료
# 2주차 20201107 코딩 시작
# 2주차 진행 중 N이 100이하가 아니면 계속 반복하는 반복문 작성이 의외로 어려웠습니다.
# 반복문:for문 이라는 생각에 사로잡혀 있다가 불현듯이 while문이 떠올랐습니다. while문 참고 https://wikidocs.net/21
# 3주차 20201113 코딩 계속
# 길이가 정해진 리스트를 선언하고 그 리스트 전체를 0으로 초기화 하는 방법을 몰라 헤맸습니다. 리스트 참고 https://jobc.tistory.com/m/141

import sys
#f = sys.stdin
f = open('data.txt', 'r')

I = 1
W, Out = 0, 0
Table = [0 for i in range(101)]

N = int(input("손님 수를 입력해주세요(100이하): "))

while N > 100:
    N = int(input("100이하로 입력해주세요: "))

for I in range(0, N, 1):
    W = int(input("원하는 자리를 입력해주세요(100이하): "))
    if Table[W] == 0:
        Table[W] = 1
    else:
        Out += 1

print("거절당한 손님의 수:", Out)