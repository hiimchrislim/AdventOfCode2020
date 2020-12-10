def get_valid_passwords(input: str) -> int:
    num_valid_passwords = 0
    for password_input in input.split("\n"):
        if password_input != "":
            col = password_input.split(" ")
            val_range = col[0].split("-")
            letter = col[1][:-1]
            min_val = True if col[2][int(val_range[0]) - 1] == letter else False
            max_val = True if col[2][int(val_range[1]) - 1] == letter else False
            if min_val ^ max_val:
                num_valid_passwords += 1
    return num_valid_passwords


if __name__ == '__main__':
    with open("input.txt") as input:
        print(get_valid_passwords(input.read()))
