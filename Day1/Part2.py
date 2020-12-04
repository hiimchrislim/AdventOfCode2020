# Returns the product of the three sum pair that sums to the targetSum (in this case 2020)
def threeSumProduct(input: str, targetSum: int):
    tripletSum = 0
    arr = []
    for num in input.split("\n"):
        if num != "":
            arr.append(int(num))
    arr.sort()
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            currentSum = arr[i] + arr[left] + arr[right]
            if currentSum == targetSum:
                tripletSum = arr[i] * arr[left] * arr[right]
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
    return tripletSum


if __name__ == '__main__':
    with open("input.txt") as input:
        print(threeSumProduct(input.read(), 2020))
