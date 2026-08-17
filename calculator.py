def main():
    while True:
        ask = input('Calculate: ').strip()
        if '+' in ask:
            print(addition(ask))
            break
        elif '-' in ask:
            print(subtraction(ask))
            break
        elif '*' in ask:
            print(multiplication(ask))
            break
        elif '/' in ask:
            print(division(ask))
            break
def addition(numbers):
    try:
        first, last = map(int, numbers.rsplit('+', 1))
    except ValueError:
        raise ValueError('Wrong Format')

    return first + last

def subtraction(numbers):
    try:
        first, last = map(int, numbers.rsplit('-', 1))
    except ValueError:
        raise ValueError('Wrong Format')

    return first - last

def multiplication(numbers):
    try:
        first, last = map(int, numbers.rsplit('*', 1))
    except ValueError:
        raise ValueError('Wrong Format')

    return first * last

def division(numbers):
    try:
        first, last = map(int, numbers.rsplit('/', 1))
        return first / last
    except ValueError:
        raise ValueError('Wrong Format')
    except ZeroDivisionError:
        raise ZeroDivisionError("Can't divide by 0")

if __name__ == '__main__':
    main()