def example1():
    num = int(input('Enter a number: '))
    if num > 1000:
        print('The input number is greater than 1000')


def example2():
    num = int(input('Enter a number: '))
    if num > 1000:
        print('The input number is greater than 1000')
    else:
        print('The input number is not greater than 1000')


def print_max_days_in_month():
    month = int(input('Enter a month number (1-12): '))
    if month < 1 or month > 12:
        print('Please input a number between 1 and 12')
    elif month == 2:
        print(f'Month {month} has 28 or 29 days')
    elif month in [4, 6, 9, 11]:
        print(f'Month {month} has 30 days')
    else:
        print(f'Month {month} has 31 days')


def print_even_odd():
    num = int(input('Enter a number: '))
    even_odd = 'even' if num % 2 == 0 else 'odd'
    print(f'{num} is an {even_odd} number')


if __name__ == '__main__':
    print_even_odd()
