def main():
    M, D = map(int, input().split())
    y, m, d = map(int, input().split())

    if d < D:
        print(f"{y} {m} {d + 1}")
        return
    if d == D and m < M:
        print(f"{y} {m + 1} 1")
        return

    print(f"{y + 1} 1 1")

main()