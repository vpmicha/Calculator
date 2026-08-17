def main():
    while True:
        ask = input('Calculate: ').strip()
        if '+' in ask:
            print(addition(ask))
        if '-' in ask:
            print(subtraction(ask))
        if '*' in ask:
            print(multiplication(ask))
        if '/' in ask:
            print(division(ask))

def addition(numbers):
    try:
        first, last = map(int, numbers.split('+'))
    except ValueError:
        raise ValueError('Wrong Format')

    return first + last

def subtraction(numbers):
    try:
        first, last = map(int, numbers.split('-'))
    except ValueError:
        raise ValueError('Wrong Format')

    return first - last

def multiplication(numbers):
    try:
        first, last = map(int, numbers.split('*'))
    except ValueError:
        raise ValueError('Wrong Format')

    return first * last

def division(numbers):
    try:
        first, last = map(int, numbers.split('/'))
        answer = first / last
    except ValueError:
        raise ValueError('Wrong Format')
    except ZeroDivisionError:
        raise ZeroDivisionError("Can't divide by 0")

    return first / last
