def main():
    n = int(input())
    s = input()
    q = int(input())
    from_str = 'abcdefghijklmnopqrstuvwxyz'
    to_str = 'abcdefghijklmnopqrstuvwxyz'

    for _ in range(q):
        c, d = input().split()
        to_str = to_str.replace(c, d)

    print(s.translate(str.maketrans(from_str, to_str)))

main()

# 以下、最初に書いた LTE となるコード
#
# def main():
#     n = int(input())
#     s = input()
#     q = int(input())

#     answer = s
#     for i in range(q):
#         c, d = input().split()
#         answer = answer.replace(c, d, -1)

#     print(answer)

# main()