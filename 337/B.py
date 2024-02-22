def main():
    s = input()
    prev = ''

    for i in range(0, len(s)):
        # 初回
        if i == 0:
            prev = s[i]
            continue
        # 変化なし
        if s[i] == prev:
            continue
        # A -> B
        if s[i] == 'B' and prev == 'A':
            prev = 'B'
            continue
        # B -> C
        if s[i] == 'C' and prev == 'B':
            prev = 'C'
            continue
        # A -> C
        if s[i] == 'C' and prev == 'A':
            prev = 'C'
            continue

        print("No")
        return

    print("Yes")

main()