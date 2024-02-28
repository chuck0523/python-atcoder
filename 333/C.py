def main():
    n = int(input())

    nums = ['1', '1', '1']

    for i in range(0, n - 1):
        print(list(map(int, nums)))

        nums[i % 3] = f"{nums[i % 3]}1"

    print(sum(int(num) for num in nums))

main()
