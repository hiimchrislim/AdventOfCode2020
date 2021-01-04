# Note: This assumes that you don't get repeat data in your passports
def get_valid_passports(input: str):
    valid_passports = 0
    count = 0
    for line in input.split("\n"):
        for key in line.split(" "):
            if key[0:3] != "cid" and key[0:3] != "":
                count += 1
            if line == "":
                if count >= 7:
                    valid_passports += 1
                count = 0
    return valid_passports


if __name__ == '__main__':
    with open("input.txt") as input:
        print(get_valid_passports(input.read()))
