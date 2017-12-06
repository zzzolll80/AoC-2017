with open("data.txt", 'r') as f:
    data = f.read()
    data_list = [item.split() for item in data.split('\n')]


def part1():
    result = 0

    for item in data_list:
        is_valid = True
        for i in range(len(item) - 1):
            for j in range(i + 1, len(item)):
                if item[i] == item[j]:
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            result += 1

    return result


def part2():
    for item in data_list:
        for i in range(len(item)):
            item[i] = list(item[i])
            item[i].sort()

    return part1()


if __name__ == '__main__':
    print('part1 :', part1())
    print('part2 :', part2())
