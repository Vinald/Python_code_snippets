def main():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    add1 = summing(num1, num2)
    print(f'{num1} + {num2} = {add1}')


def summing(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    main()
