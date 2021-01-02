def get_trees_encountered(input: str, right: int, down: int):
    is_right = True
    position = 0
    trees_encountered = 0
    line_count = 0
    for count, i in enumerate(input.split('\n'), start=0):
        if i != "" and count % down == 0:
            if not is_right:
                if i[position] == "#":
                    trees_encountered += 1
                is_right = True
            if is_right:
                position = (position + right) % len(i)
                is_right = False
                line_count = (line_count + 1) % down
                if line_count != 0:
                    continue
    return trees_encountered


if __name__ == '__main__':
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for slope in slopes:
        with open("input.txt") as input:
            val = get_trees_encountered(input.read(), slope[0], slope[1])
            product *= val
            input.close()
    print(product)
