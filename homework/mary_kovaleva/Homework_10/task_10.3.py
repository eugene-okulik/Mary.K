from functools import wraps


def choose_func(func):
    @wraps(func)
    def wrapper(*args):
        num1, num2, symbol = args
        match(num1, num2):
            case(num1, num2) if num1 < 0 or num2 < 0: symbol = '*'
            case (num1, num2) if num1 == num2: symbol = '+'
            case (num1, num2) if num1 < num2: symbol = '/'
            case (num1, num2) if num1 > num2: symbol = '-'
        return f"Result: {func(num1, num2, symbol)}"
    return wrapper


@choose_func
def calc(first, second, operation):
    match operation:
        case '+': return first + second
        case '-': return first - second
        case '/': return first / second
        case '*': return first * second


print(calc(int(input('Number 1: ')), int(input('Number 2: ')), input('Symbol: ')))
