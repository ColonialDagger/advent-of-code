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
    n = len(data)
    m = len(data[0])

    def is_symbol(i, j):
        if not (0 <= i < n and 0 <= j < m):  # Prevents Index errors
            return False

        return data[i][j] != "." and not data[i][j].isdigit()

    for i, line in enumerate(data):
        start = 0
        j = 0

        while j < m:
            start = j
            num = ""
            while j < m and line[j].isdigit():
                num += line[j]
                j += 1

            if num == "":
                j += 1
                continue

            num = int(num)

            if is_symbol(i, start-1) or is_symbol(i, j):
                ans += num
                j += 1
                continue

            for k in range(start-1, j+1):
                if is_symbol(i-1, k) or is_symbol(i+1, k):
                    ans += num
                    break

    return ans

def part2(data: list):
    ans = 0
    n = len(data)
    m = len(data[0])

    goods = [[[] for _ in range(m)] for _ in range(n)]

    def is_symbol(i, j, num):
        if not (0 <= i < n and 0 <= j < m):  # Prevents Index errors
            return False
        if data[i][j] == "*":
            goods[i][j].append(num)

        return data[i][j] != "." and not data[i][j].isdigit()

    for i, line in enumerate(data):
        start = 0
        j = 0

        while j < m:
            start = j
            num = ""
            while j < m and line[j].isdigit():
                num += line[j]
                j += 1

            if num == "":
                j += 1
                continue

            num = int(num)

            # Number ended, look around
            is_symbol(i, start - 1, num) or is_symbol(i, j, num)

            for k in range(start-1, j+1):
                is_symbol(i-1, k, num) or is_symbol(i+1, k, num)

    for i in range(n):
        for j in range(m):
            nums = goods[i][j]
            if data[i][j] == '*' and len(nums) == 2:
                ans += nums[0] * nums[1]

    return ans

if __name__ == "__main__":

    DAY = 3
    YEAR = 2023

    data = get_data(DAY, YEAR)

    ans1 = part1(data)
    aocd.submit(ans1, part="a", day=DAY, year=YEAR)

    ans2 = part2(data)
    aocd.submit(ans2, part="b", day=DAY, year=YEAR)
