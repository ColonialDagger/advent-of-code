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

    left = []
    right = []
    for line in data:
        line = line.split(' ')
        left.append(line[0])
        right.append(line[3])

    left.sort()
    right.sort()

    for i in range(len(left)):
        sum += abs(int(left.pop(0)) - int(right.pop(0)))
    
    return sum

def part2(data: list):
    sum = 0

    left = []
    right = []
    for line in data:
        line = line.split(' ')
        left.append(line[0])
        right.append(line[3])

    right_sorted = {}
    for line in right:
        try:
            right_sorted[line] += 1
        except KeyError:
            right_sorted[line] = 1

    for line in left:
        try:
            sum += int(line) * right_sorted[line]
        except KeyError:
            sum += 0
    
    return sum

if __name__ == "__main__":

    DAY = 1
    YEAR = 2024

    data = get_data(DAY, YEAR)

    ans1 = part1(data)
    aocd.submit(ans1, part="a", day=DAY, year=YEAR)

    ans2 = part2(data)
    aocd.submit(ans2, part="b", day=DAY, year=YEAR)
    