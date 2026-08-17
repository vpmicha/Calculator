def main():
    while True:
        ask = input('Calculate: ').strip()
        if '+' in ask:
            print(addition(ask))
            break
        if '-' in ask:
            print(subtraction(ask))
            break
        if '*' in ask:
            print(multiplication(ask))
            break
        if '/' in ask:
            print(division(ask))
            break
def addition(numbers):
    numbers_list = []
    try:
        if numbers.count('+') > 1:
            numbers_list.append(numbers.split('+'))
            return numbers_list[1] - numbers_list[2]
        first, last = map(int, numbers.split('+'))
    except ValueError:
        raise ValueError('Wrong Format')

    return first + last

def subtraction(numbers):
    numbers_list = []
    try:
        if numbers.count('-') > 1:
            numbers_list.append(numbers.split('-'))
            return numbers_list[1] - numbers_list[2]
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

    return answer

if __name__ == '__main__':
    main()