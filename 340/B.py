import math

def main():
    a = []
    count = int(input())

    for _ in range(count):
        query, x = map(int, input().split())

        if query == 1:
            a.append(x)

        if query == 2:
            print(a[x*-1])

main()