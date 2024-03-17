def main():
    n = int(input())
    persons = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        a, b = map(int, input().split())

        a_pos = persons.index(a)
        b_pos = persons.index(b)
        if a_pos < b_pos:
            print(a)
        else:
            print(b)

main()