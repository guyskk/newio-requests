import functools
from newio_kernel import run


def run_with_newio(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        run(f(*args, **kwargs), timeout=10)
    return wrapper
