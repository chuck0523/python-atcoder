def main():
    n, l, r = map(int, input().split())
    nums = list(map(int, input().split()))

    result = []
    for i in range(n):
        num = nums[i]

        if num < l:
            result.append(str(l))
            continue
        if num > r:
            result.append(str(r))
            continue

        result.append(str(num))

    print(' '.join(result))

main()
