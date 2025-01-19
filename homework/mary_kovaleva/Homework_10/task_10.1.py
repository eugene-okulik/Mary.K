from functools import wraps


def finish_me(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
