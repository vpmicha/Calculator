def main():
    while True:
        ask = input('Calculate: ').strip()
        if '+' in ask:
            addition(ask)
        if '-' in ask:
            subtraction(ask)
        if '*' in ask:
            multiplication(ask)
        if '/' in ask:
            division(ask)

