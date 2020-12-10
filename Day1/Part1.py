# Returns the product of the two sum pair that sums to the targetSum (in this case 2020)
def two_sum_product(input: str, target_sum):
    pairs = {}
    for num in input.split("\n"):
        if num != "":
            num = int(num)
            if num not in pairs and abs(target_sum-num) not in pairs:
                pairs[num] = 1
            else:
                return num * (target_sum - num)
    return -1


if __name__ == '__main__':
    with open("Day1/input.txt") as input:
        print(two_sum_product(input.read(), 2020))
