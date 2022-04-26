def nd_dir(obj):
    for atr in dir(obj):
        if not atr.startswith('_'):
            print(atr, end=', ')
    print()


if __name__ == '__main__':
    nd_dir('vinod')
    print('-'*50)
    nd_dir(123)
    print('-'*50)
    nd_dir(False)
    print('-'*50)
    nd_dir(1.2)
    print('-'*50)
