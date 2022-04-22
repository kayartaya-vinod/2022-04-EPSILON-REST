from user_defined_functions_demo import square


if __name__ == '__main__':
    num = 19
    sq = square(num)
    print(f'Square of {num} is {sq}')

    # __name__ is a python builtin variable, representing the name of the module
    # __name__ will be equal to '__main__' if you are executing the script, but
    # if you are importing a script __name__ is equal to the name of the file itself (without .py)
    print(f'Inside module_demo.py, value of __name__ is {__name__}')
