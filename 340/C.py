import math

def main():
    n = int(input())
    nums = [n]

    result = 0

    while len(nums) > 0:
        x = nums[0]
        result += x
        nums.pop(0)
        if math.floor(x / 2) >= 2:
            nums.append(math.floor(x / 2))
        if math.ceil(x / 2) >= 2:
            nums.append(math.ceil(x / 2))

    print(result)

main()