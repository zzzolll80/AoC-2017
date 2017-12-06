with open("data.txt", 'r') as f:
    data = f.read()

find_dict = {}
data_list = [int(item) for item in data.split('\t')]


def part1():
    while True:
        if find_dict.get(str(data_list)) is not None:
            return len(find_dict)
        else:
            find_dict[str(data_list)] = len(find_dict)

        max_value = max(data_list)
        max_index = data_list.index(max_value)
        data_list[max_index] = 0

        while max_value > 0:
            max_index += 1
            if max_index == len(data_list):
                max_index = 0
            data_list[max_index] += 1
            max_value -= 1


def part2():
    return part1() - find_dict.get(str(data_list))


if __name__ == '__main__':
    print('part1 :', part1())
    print('part2 :', part2())
