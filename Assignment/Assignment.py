# 1주차 20201031 문제 분석 및 알고리즘 순서도 작성: 완료
# 2주차 20201107 코딩 시작
# 2주차 진행 중 N이 100이하가 아니면 계속 반복하는 반복문 작성이 의외로 어려웠습니다.
# 반복문:for문 이라는 생각에 사로잡혀 있다가 도저히 생각이 안나 while문을 활용했습니다. while문 참고 https://wikidocs.net/21


import sys
#f = sys.stdin
f = open('data.txt', 'r')

I = 1
W, Out = 0, 0
Table = [0]

N = int(input("손님 수를 입력해주세요(100이하): "))

while N > 100:
    N = int(input("100이하로 입력해주세요: "))

for I in range(1, N, 1):
    W = int(input("원하는 자리를 입력해주세요(100이하): "))
    if Table[W] == 0:
        print('test')
    else:
        Out += 1
