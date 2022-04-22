# A function is a block of code that is reusable, by supplying different values as parameters.

# defining/creating function here
def say_hello():
    print('Hello')
    print('How are you?')


def greet():
    print('Greetings from Vinod!')


def square(num):
    sq = num*num
    return sq


# the following condition is True only if you execute this script file
# and False if this file is imported in another module which is being executed.
if __name__ == '__main__':
    # calling/invoking/executing the functions here
    say_hello()
    greet()
    s = square(23)
    print(f'square of 23 is {s}')
    s = square(15)
    print(f'square of 15 is {s}')
    s = square(56)
    print(f'square of 56 is {s}')

    print(f'Inside user_defined_functions_demo.py, value of __name__ is {__name__}')
