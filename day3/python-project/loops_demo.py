def while_loop_example():
    num = int(input('Enter a number: '))
    i = 1
    print('-'*50)

    while i <= 10:
        print(f'{num} X {i} = {num*i}')
        i = i + 1

    print('-'*50)


def for_loop_example1():
    for ch in 'Vinod Kumar':
        print(ch)


def for_loop_example2():
    for n in [12, 34, 59, 75, 99, 123, 345]:
        print(f'Square of {n} is {n*n}')


def for_loop_example3():
    num = int(input('Enter a number: '))
    for i in range(1, 11):  # represents a range of values from 1 to 11-1 (i.e, 10)
        print(f'{num} X {i} = {num * i}')


def range_example1():
    for i in range(10):  # --> 0 to 9
        print(i, end=', ')
    print()

    for i in range(5, 10):  # --> 5, 9
        print(i, end=', ')
    print()

    for i in range(3, 25, 5):  # --> 3, 8, 13, 18, 23
        print(i, end=', ')
    print()


if __name__ == '__main__':
    range_example1()
