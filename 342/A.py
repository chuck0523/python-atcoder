def main():
    s = input()

    # 1,2,3文字目が一緒
    if s[0] == s[1] and s[1] == s[2]:
        same = s[0]
        for i in range(3, len(s)):
            if s[i] != same:
                print(i + 1)
                return

    # 1,2文字目が一緒
    if s[0] == s[1]:
        print(3)
        return

    # 2,3文字目が一緒
    if s[1] == s[2]:
        print(1)
        return

    # 1,3文字目が一緒
    if s[0] == s[2]:
        print(2)
        return

main()