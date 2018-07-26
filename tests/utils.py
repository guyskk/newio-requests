import functools
from newio import Runner


run = Runner(debug=True)


def run_with_newio(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        run(f, *args, **kwargs)

    return wrapper
