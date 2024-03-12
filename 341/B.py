import math

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n - 1):
        # 為替レート
        prev, next = map(int, input().split())

        # 何単元を交換可能か
        count = math.floor(nums[i] / prev)

        # 交換の実行
        nums[i] -= count * prev
        nums[i+1] += count * next

    print(nums[-1])

main()