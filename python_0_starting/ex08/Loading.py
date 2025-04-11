import sys
from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    for i, val in enumerate(lst, 1):
        percent = int((i / total) * 100)
        bar_len = 69
        filled_len = int(i * bar_len // total)
        bar = "=" * filled_len + ">" + " " * (bar_len - filled_len)
        sys.stdout.write(f"\r{percent}%|[{bar}]| {i}/{total}")
        yield val  # 👈 retourne chaque élément un par un
    print()  # aller à la ligne à la fin


def main():
    """main function"""
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if main.__name__:
    main()
