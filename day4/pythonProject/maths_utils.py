def value_of(str_num):
    try:
        return float(str_num)
    except ValueError:
        return 0


def calculate_sum(str_nums):
    if type(str_nums) != str:
        raise ValueError('Input was not a str while expecting a str')

    return sum([value_of(s) for s in str_nums.split(',')])


def main():
    total = calculate_sum('10, 30, 40.2, vinod, False, None, 20, 40')
    print(total)

    total = calculate_sum(123)
    print(total)


if __name__ == '__main__':
    main()
