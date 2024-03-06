def main():
    d = int(input())

    result = d
    for i in range(10000):
        for j in range(10000):
            num = abs(i*i + j*j - d)
            if num < result:
                result = num

    print(result)

main()