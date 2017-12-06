with open("data.txt", 'r') as f:
    data = f.read()


def part1():
    result = 0
    current = int(data[-1])

    for i in data:
        previous = current
        current = int(i)

        if current == previous:
            result += current

    print('part1 :', result)


def part2():
    result = 0
    half = len(data) // 2
    for i in range(-half, half):
        if data[i] == data[i + half]:
            result += int(data[i])

    print('part2 :', result)


if __name__ == '__main__':
    part1()
    part2()
