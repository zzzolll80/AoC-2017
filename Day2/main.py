with open("data.txt", 'r') as f:
    data = f.read()


def part1():
    result = 0

    str_list = data.split('\n')
    for i in range(len(str_list)):
        max_v = 0
        min_v = 10000
        str_list[i] = str_list[i].split('\t')
        for el in str_list[i]:
            if max_v < int(el):
                max_v = int(el)
            if min_v > int(el):
                min_v = int(el)
        result += max_v - min_v

    print('part1 :', result)


def part2():
    result = 0
    skip = False
    str_list = data.split('\n')
    for x in range(len(str_list)):
        str_list[x] = str_list[x].split('\t')
        for i in range(len(str_list[x])):
            for j in range(i + 1, len(str_list[x])):
                if max(int(str_list[x][i]), int(str_list[x][j])) % min(int(str_list[x][i]), int(str_list[x][j])) == 0:
                    result += max(int(str_list[x][i]), int(str_list[x][j])) // min(int(str_list[x][i]), int(str_list[x][j]))
                    skip = True
                    break
            if skip:
                break
        skip = False

    print('part2 :', result)


if __name__ == '__main__':
    part1()
    part2()
