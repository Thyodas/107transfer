import sys


def print_help():
    print("""USAGE
    ./107transfer [num den]*
DESCRIPTION
    num     polynomial numerator defined by its coefficients
    den     polynomial denominator defined by its coefficients""")


def calculate_polynom(x, coef: list[float]):
    result = coef[-1]
    for i in reversed(range(len(coef) - 1)):
        result = result * x + coef[i]
    return result


def calculate(num_list, den_list):
    x = 0
    while x <= 1:
        result = 1
        for i in range(len(num_list)):
            num = calculate_polynom(x, num_list[i])
            den = calculate_polynom(x, den_list[i])
            if den == 0:
                print("Division by zero.")
                sys.exit(84)
            result *= num / den
        print(f"{x:.3f} -> {result:.5f}")
        x = round(x + 0.001, 3)


def argument_handler(args):
    if "-h" in args:
        print_help()
        sys.exit(0)
    try:
        if len(args) % 2 != 0 or len(args) < 2:
            print("Wrong number of arguments. Must be even.")
            sys.exit(84)
        for arg in args:
            for letter in arg:
                if letter not in "0123456789*.":
                    print("Wrong symbol.")
                    sys.exit(84)
            if arg[0] == '*' or arg[-1] == '*':
                print("Argument should start and end with a number.")
                sys.exit(84)
        num = []
        den = []
        turn = True
        for i in range(len(args)):
            if turn:
                num.append(list(map(float, args[i].split("*"))))
            else:
                den.append(list(map(float, args[i].split("*"))))
            turn = not turn
        calculate(num, den)
    except ValueError:
        print("Wrong arguments. Need numbers.")
        sys.exit(84)


if __name__ == "__main__":
    argument_handler(sys.argv[1:])
