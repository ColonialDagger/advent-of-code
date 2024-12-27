from operator import truediv

import aocd


def get_data(day: int, year: int) -> list:
    try:
        with open(f'day{day}.txt', 'r') as f:
            return f.read().split('\n')
    except FileNotFoundError:
        data = aocd.get_data(day=DAY, year=YEAR)
        with open(f'day{day}.txt', 'w') as f:
            f.writelines(data)
        return data.splitlines()


def part1(data: list):
    sum = 0

    for line in data:
        line = [int(x) for x in line.split(' ')]

        # Check if sorted
        sort = sorted(line)
        if sort == line or sort.reverse() == line:  # Line is all increasing or decreasing

            # Build diffs
            diffs = []
            last = 0
            for i in line:
                diffs.append(i - last)
                last = i

            diffs.pop(0)
            for i in diffs:
                safe = []
                if 1 <= abs(i) <= 3:
                    safe.append(True)
                else:
                    safe.append(False)
                    continue

            # Check if diffs are all within ranges
            print()
            if all(safe):
                sum += 1

    return sum


def part2(data: list):
    sum = 0

    return sum


if __name__ == "__main__":
    DAY = 2
    YEAR = 2024

    data = get_data(DAY, YEAR)

    ans1 = part1(data)
    aocd.submit(ans1, part="a", day=DAY, year=YEAR)

    ans2 = part2(data)
    aocd.submit(ans2, part="b", day=DAY, year=YEAR)
