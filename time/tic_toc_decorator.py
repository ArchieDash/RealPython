import time
from reader import feed


def tic_toc(func):
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        func()
        toc = time.perf_counter()
        print(f"\n\n{func.__name__} executed within {toc - tic:0.4f} seconds")
    return wrapper


@tic_toc
def main():
    tutorial = feed.get_article(1)
    print(tutorial)
    
    
if __name__ == "__main__":
    main()
