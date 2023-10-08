import math

C = int(input())

for _ in range(C):
    # 리스트에다가 다 입력 받기
    ary = input().split()
    # 입력 받은 첫 번째 문자열을 S에다가 넣음
    S = ary[0]
    # 받은 나머지 부분을 다 나눠서 분배
    N, T, L = map(int, ary[1:])
    maxTime = (10 ** 8) * L

    if S == "O(N)":
        if N * T  <=  maxTime:
            print("May Pass.")
        else:
            print("TLE!")

    if S == "O(N^2)":
        if (N ** 2) * T <= maxTime:
            print("May Pass.")
        else:
            print("TLE!")

    if S == "O(N^3)":
        if (N ** 3) * T <= maxTime:
            print("May Pass.")
        else:
            print("TLE!")

    if S == "O(2^N)":
        if (2 ** N) * T <= maxTime:
            print("May Pass.")
        else:
            print("TLE!")

    if S == "O(N!)":
        if math.factorial(N) * T <= maxTime:
            print("May Pass.")
        else:
            print("TLE!")