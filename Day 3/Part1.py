def get_trees_encountered(input: str):
    is_right = True
    position = 0
    trees_encountered = 0
    # The entire path is (Move 3 right and 1 down before checking)
    for i in input.split('\n'):
        if i != "":
            if not is_right:
                if i[position] == "#":
                    trees_encountered += 1
                # You still move right on the path that you went down on
                is_right = True
            if is_right:
                position = (position + 3) % len(i)
                is_right = False
    return trees_encountered


if __name__ == '__main__':
    with open("input.txt") as input:
        print(get_trees_encountered(input.read()))
