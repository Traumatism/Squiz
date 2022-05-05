from squiz.squiz import run
from squiz.logger import console


if __name__ == "__main__":

    try:
        run()
    except Exception:
        console.print_exception()
