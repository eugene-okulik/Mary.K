from functools import wraps


def repeat_me(**kwargs):

    def real_decorator(func):
        @wraps(func)
        def wrapper(*args):
            for i in range(kwargs['count']):
                func(*args)
        return wrapper
    return real_decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
