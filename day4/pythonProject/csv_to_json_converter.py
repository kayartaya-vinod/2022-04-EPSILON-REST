"""
CSV to JSON converter
This module demonstrates the power of list comprehension, file handling and exception handling
"""
import json


def main():
    """
    In this function, we will accept the name of the input CSV file, and using list comprehension and some
    dictionary utilities, we will create a new JSON file consisting of same data.
    """
    filename = input('Enter CSV filename: ')
    # f = open(filename, 'r')
    # for line in f:
    #     print(line, end='')
    # f.close()

    # using a context manager; closes all resources when the context manager exits.
    # with open(filename, 'r') as f:
    #     for line in f:
    #         print(line, end='')

    with open(filename, 'r') as f:
        header = f.readline().strip().split(',')  # first line
        # data = list()
        #
        # for line in f:
        #     value = line.strip().split(',')
        #     d = dict(zip(header, value))
        #     data.append(d)
        data = [dict(zip(header, line.strip().split(','))) for line in f]

    with open('OUTPUT.json', 'w') as f:
        json.dump(data, f)

    print('JSON data written to OUTPUT.json file')


if __name__ == '__main__':
    main()
