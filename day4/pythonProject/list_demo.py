def main():
    data = [3, 100, 55, 34, 12, 56, 5, 1, 78, 239, 48, 99, 222, 239, 2, 777, 4]

    even_numbers = []
    for n in data:
        if n % 2 == 0:
            even_numbers.append(n)

    # list comprehension
    odd_numbers = [n for n in data if n % 2]

    print(f'data is {data}')
    print(f'even_numbers is {even_numbers}')
    print(f'odd_numbers is {odd_numbers}')

    squares = [n*n for n in data]
    print(f'squares is {squares}')


if __name__ == '__main__':
    main()
