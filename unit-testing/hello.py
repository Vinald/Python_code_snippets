def main():
    name = input('Enter your name: ')
    output = hello(name)
    print(output)


def hello(name='samuel'):
    return f'hello {name}'


if __name__ == '__main__':
    main()
