import math

with open("data.txt", 'r') as f:
    data = f.read()


def part1():
    input_number = int(data)

    result = 0

    sqr_len = math.ceil(input_number ** 0.5)
    half_len = sqr_len // 2
    result += half_len

    if sqr_len % 2 == 0:
        sqr_len += 1

    result += min([abs(input_number - (sqr_len ** 2 - half_len * i)) for i in range(1, 8, 2)])

    print('part1 :', result)


def part2():
    result = 0
    for i in range(5):
        result += i
    print('part2 :', result)


if __name__ == '__main__':
    part1()
    part2()
