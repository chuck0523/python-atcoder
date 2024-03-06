def main():
    n, l = map(int, input().split())
    answers = map(int, input().split())
    print(len(list(filter(lambda a: a >= l, answers))))

main()