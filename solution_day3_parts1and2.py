import re


def solve_part_one(memory):
    """
    Part 1:
    Find every valid mul(X,Y), where X and Y are 1-3 digit numbers.
    Sum X * Y for all valid instructions.
    """
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0
    for match in re.finditer(pattern, memory):
        left = int(match.group(1))
        right = int(match.group(2))
        total += left * right
    return total


def solve_part_two(memory):
    """
    Part 2:
    Process the memory from left to right.
    - mul(X,Y) counts only when multiplication is enabled.
    - do() enables future mul instructions.
    - don't() disables future mul instructions.
    - multiplication starts enabled.
    """
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    enabled = True
    total = 0
    for match in re.finditer(pattern, memory):
        instruction = match.group(0)
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            if enabled:
                left = int(match.group(1))
                right = int(match.group(2))
                total += left * right
    return total


def parse_input(path):
    """
    Reads the full corrupted memory as one string.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    input_file = "input.txt"
    memory = parse_input(input_file)
    part_one_answer = solve_part_one(memory)
    part_two_answer = solve_part_two(memory)
    print("Part 1:", part_one_answer)
    print("Part 2:", part_two_answer)


if __name__ == "__main__":
    main()
