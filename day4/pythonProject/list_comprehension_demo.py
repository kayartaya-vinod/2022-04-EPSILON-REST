def main():
    data = [12, 304, 'vinod', False, '40', 49, 593, 456, 234, 'robert']
    num_data = [n for n in data if type(n) in (int, float)]
    total = sum(num_data)
    print(f'Sum of {num_data} is {total}')


if __name__ == '__main__':
    main()
