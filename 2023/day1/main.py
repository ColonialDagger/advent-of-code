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

        for char in line:
            try:
                front = int(char)
                break
            except ValueError:
                continue

        for char in reversed(line):
            try:
                back = int(char)
                break
            except ValueError:
                continue

        sum += front * 10 + back

    return sum

def part2(data: list):
    sum = 0
    words = [
        ['one', '1'],
        ['two', '2'],
        ['three', '3'],
        ['four', '4'],
        ['five', '5'],
        ['six', '6'],
        ['seven', '7'],
        ['eight', '8'],
        ['nine', '9']
    ]
    for line in data:
        for word, num in words:
            line = line.replace(word, f"{word}{num}{word}")
        sum += part1([line])
    return sum

if __name__ == "__main__":

    DAY = 1
    YEAR = 2023

    data = get_data(DAY, YEAR)

    ans1 = part1(data)
    aocd.submit(ans1, part="a", day=DAY, year=YEAR)

    ans2 = part2(data)
    aocd.submit(ans2, part="b", day=DAY, year=YEAR)
