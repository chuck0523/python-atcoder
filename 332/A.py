def main():
    n, s, k = map(int, input().split())

    sum = 0
    for _ in range(0, n):
        p, q = map(int, input().split())
        sum += p * q

    if sum < s:
        sum += k

    print(sum)

main()