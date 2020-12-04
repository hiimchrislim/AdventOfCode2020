# Returns the product of the two sum pair that sums to 2020
def twoSumProduct(input: str):
    pairs = {}
    for num in input.split("\n"):
        if num != "":
            num = int(num)
            if num not in pairs and abs(2020-num) not in pairs:
                pairs[num] = 1
            else:
                return num * (2020 - num)
    return -1


if __name__ == '__main__':
    with open("Day1/partOneInput.txt") as input:
        print(twoSumProduct(input.read()))
