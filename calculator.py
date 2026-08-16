import sys

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