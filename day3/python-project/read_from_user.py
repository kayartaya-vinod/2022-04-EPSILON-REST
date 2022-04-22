name = input('What\'s your name? ')
city = input('Where are you from? ')
age = input('How old are you? ')  # <class str>
age = int(age)  # convert to <class int>

print('-' * 50)
print(f'{name} from {city} is {age} years old.')
print(f'After 7 years, {name} will be {age + 7} years old.')
print('-' * 50)
