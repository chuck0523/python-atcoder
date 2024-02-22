def main():
    n = int(input())

    T = 0
    A = 0
    for i in range(0, n):
        t, a = list(map(int, input().split()))
        T += t
        A += a

    if T > A:
        print("Takahashi")
    elif T < A:
        print("Aoki")
    else:
        print("Draw")

main()