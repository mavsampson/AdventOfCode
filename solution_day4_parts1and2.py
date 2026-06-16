def parse_input(path):
    """
    Reads the word-search grid from the input file.
    Each line is one row of the grid.
    """
    with open(path, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def count_xmas_part_one(grid):
    """
    Part 1:
    Count every occurrence of XMAS in all 8 directions:
    - horizontal
    - vertical
    - diagonal
    - forward and backward
    """
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    total = 0
    for row in range(rows):
        for col in range(cols):
            for row_step, col_step in directions:
                found = True
                for i in range(word_len):
                    new_row = row + i * row_step
                    new_col = col + i * col_step
                    if (
                        new_row < 0
                        or new_row >= rows
                        or new_col < 0
                        or new_col >= cols
                        or grid[new_row][new_col] != word[i]
                    ):
                        found = False
                        break
                if found:
                    total += 1
    return total


def count_x_mas_part_two(grid):
    """
    Part 2:
    Count X-MAS patterns.
    An X-MAS has:
    - A at the center
    - one diagonal spelling MAS or SAM
    - the other diagonal also spelling MAS or SAM
    Example:
    M.S
    .A.
    M.S
    """
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] != "A":
                continue
            diagonal_one = (
                grid[row - 1][col - 1]
                + grid[row][col]
                + grid[row + 1][col + 1]
            )
            diagonal_two = (
                grid[row - 1][col + 1]
                + grid[row][col]
                + grid[row + 1][col - 1]
            )
            if diagonal_one in ("MAS", "SAM") and diagonal_two in ("MAS", "SAM"):
                total += 1
    return total


def main():
    input_file = "input.txt"
    grid = parse_input(input_file)
    part_one_answer = count_xmas_part_one(grid)
    part_two_answer = count_x_mas_part_two(grid)
    print("Part 1:", part_one_answer)
    print("Part 2:", part_two_answer)


if __name__ == "__main__":
    main()
