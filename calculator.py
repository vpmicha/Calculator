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
