# Returns the product of the three sum pair that sums to the target_sum (in this case 2020)
def three_sum_product(input: str, target_sum: int):
    triplet_sum = 0
    arr = []
    for num in input.split("\n"):
        if num != "":
            arr.append(int(num))
    arr.sort()
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                return arr[i] * arr[left] * arr[right]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return triplet_sum


if __name__ == '__main__':
    with open("input.txt") as input:
        print(three_sum_product(input.read(), 2020))
