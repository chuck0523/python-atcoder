def main():
    n = int(input())
    s = input().split()

    # 最初の人の位置
    prev = str(s.index('-1') + 1)

    # 人々の列
    people = prev

    for i in range(0, n - 1):
        # 次の人を探す
        target = str(int(s.index(prev)) + 1)
        people += ' '
        people += target
        prev = target

    print(people)

main()