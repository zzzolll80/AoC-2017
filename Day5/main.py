with open("data.txt", 'r') as f:
    data = f.read()


def part1():
    result = 0
    current = 0
    data_list = [int(item) for item in data.split('\n')]

    while 0 <= current < len(data_list):
        result += 1
        data_list[current] += 1
        current += data_list[current] - 1

    return result


def part2():
    result = 0
    current = 0
    data_list = [int(item) for item in data.split('\n')]

    while 0 <= current < len(data_list):
        result += 1

        if data_list[current] >= 3:
            data_list[current] -= 1
            current += data_list[current] + 1
        else:
            data_list[current] += 1
            current += data_list[current] - 1

    return result


if __name__ == '__main__':
    print('part1 :', part1())
    print('part2 :', part2())
