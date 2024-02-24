def main():
    n = int(input())
    b = bin(n)[2:]

    endOfZero = str(b)[::-1].index("1")
    print(endOfZero)

main()
