def main():
    S = input()

    if S[0].islower():
        print("No")
        return

    for i in range(len(S) - 1):
        if S[i+1].isupper():
            print("No")
            return

    print("Yes")

main()