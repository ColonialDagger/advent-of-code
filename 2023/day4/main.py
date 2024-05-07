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
    ans = 0

    for line in data:
        card = line.split(': ')[0].replace('Card', '').replace(' ', '')
        left = line.split(': ')[1].split(' | ')[0].split(' ')
        right = line.split(': ')[1].split(' | ')[1].split(' ')
        winners = 0
        score = 0

        for number in right:
            if number == '':
                continue
            if number in left:
                winners += 1

        if winners > 0:
            score = 1
            winners -= 1

            while winners > 0:
                score *= 2
                winners -= 1

        ans += score

    return ans


def part2(data: list):
    ans = 0

    queue = data
    while len(queue) > 0:
        card = data.pop(0)
        score = part1([card])
        print()




    return ans


if __name__ == "__main__":
    DAY = 4
    YEAR = 2023

    data = get_data(DAY, YEAR)

    ans1 = part1(data)
    aocd.submit(ans1, part="a", day=DAY, year=YEAR)

    ans2 = part2(data)
    aocd.submit(ans2, part="b", day=DAY, year=YEAR)
