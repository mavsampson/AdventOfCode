def parse_input(path):
    """
    Reads the puzzle input file.
    Each line is one report.
    Each report contains space-separated integer levels.
    """
    with open(path, "r", encoding="utf-8") as file:
        reports = [
            list(map(int, line.split()))
            for line in file
            if line.strip()
        ]
    return reports


def is_safe(report):
    """
    Part 1 rule.
    A report is safe if:
    - the levels are strictly increasing or strictly decreasing
    - every adjacent difference is at least 1 and at most 3
    """
    diffs = [
        report[i + 1] - report[i]
        for i in range(len(report) - 1)
    ]
    increasing = all(1 <= diff <= 3 for diff in diffs)
    decreasing = all(-3 <= diff <= -1 for diff in diffs)
    return increasing or decreasing


def is_safe_with_dampener(report):
    """
    Part 2 rule.
    A report is safe if:
    - it is already safe, or
    - removing exactly one level makes it safe
    """
    if is_safe(report):
        return True
    for index in range(len(report)):
        reduced_report = report[:index] + report[index + 1:]
        if is_safe(reduced_report):
            return True
    return False


def solve_part_one(reports):
    """
    Counts reports that are safe under the original rules.
    """
    return sum(is_safe(report) for report in reports)


def solve_part_two(reports):
    """
    Counts reports that are safe with the Problem Dampener.
    """
    return sum(is_safe_with_dampener(report) for report in reports)


def main():
    input_file = "input.txt"
    reports = parse_input(input_file)
    part_one_answer = solve_part_one(reports)
    part_two_answer = solve_part_two(reports)
    print("Part 1:", part_one_answer)
    print("Part 2:", part_two_answer)


if __name__ == "__main__":
    main()
