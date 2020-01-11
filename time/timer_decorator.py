import functools
import time
from reader import feed


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer


if __name__ == "__main__":
    @timer
    def latest_tutorial():
        tutorial = feed.get_article(0)
        print(tutorial)
    latest_tutorial()