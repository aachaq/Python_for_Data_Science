import sys


def ft_tqdm(lst: range):
    """
    une fonction qui simule le fonctionnement de la fonction tqdm().
    """
    total = len(lst)
    for i, val in enumerate(lst, 1):  # pour indixer a 1 au lieux de 0
        percent = int((i / total) * 100)
        bar_len = 76
        filled_len = int(i * bar_len // total)
        bar = "=" * filled_len + ">" + " " * (bar_len - filled_len)
        sys.stdout.write(f"\r{percent}%|[{bar}]| {i}/{total}")
        yield val  # retourne chaque élément un par un
    print()
