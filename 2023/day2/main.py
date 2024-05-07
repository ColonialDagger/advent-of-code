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

    max_dice = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for line in data:
        line = line.split(': ')

        game = line[0].split(' ')[1]
        rounds = line[1].split('; ')

        try:
            for round in rounds:
                results = round.split(', ')
                for dice in results:
                    dice = dice.split(' ')
                    if int(dice[0]) > max_dice[dice[1]]:
                        raise ValueError
            sum += int(game)
        except ValueError:
            continue

    return sum

def part2(data: list):
    sum = 0

    for line in data:

        max_dice = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        line = line.split(': ')

        game = line[0].split(' ')[1]
        rounds = line[1].split('; ')

        for round in rounds:
            results = round.split(', ')
            for dice in results:
                dice = dice.split(' ')
                if int(dice[0]) > max_dice[dice[1]]:
                    max_dice[dice[1]] = int(dice[0])

        power = 1
        for key in max_dice:
            power *= max_dice[key]

        sum += power

    return sum

if __name__ == "__main__":

    DAY = 2
    YEAR = 2023

    data = get_data(DAY, YEAR)

    ans1 = part1(data)
    aocd.submit(ans1, part="a", day=DAY, year=YEAR)

    ans2 = part2(data)
    aocd.submit(ans2, part="b", day=DAY, year=YEAR)
