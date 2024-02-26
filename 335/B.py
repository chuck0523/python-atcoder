def main():
    n = int(input())

    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                x, y, z = i, j, k
                if x + y + z <= n:
                    print(x, y, z)
                if x == n:
                    return

main()