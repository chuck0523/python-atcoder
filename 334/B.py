import math

# TLE
# def main():
#     a, m, l, r = map(int, input().split())
#
#     result = 0
#     for i in range(l, r + 1):
#         # 基準点からの距離がmの倍数なら、ツリーが植わっているはず
#         if abs(a - i) % m == 0:
#             result +=1
#
#     print(result)
#
# main()

def main():
    a, m, l, r = map(int, input().split())

    start, end = 0, 0
    for i in range(l, r + 1):
        if abs(a - i) % m == 0:
            start = i
            break
    for i in range(r, l + 1, -1):
        if abs(a - i) % m == 0:
            end = i
            break

    if abs(end - start) == 0:
        print(0)
    else:
        print(math.ceil((end - start) / m) + 1)

main()