from timer import Timer
from reader import feed


def main():
    with Timer():
        tutorial = feed.get_article(1)
        print(tutorial)
    
if __name__ == "__main__":
    main()