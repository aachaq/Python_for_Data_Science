import sys
import string


def building_print():
    """
    fonction qui compte  le nombre des majuscules,
    des minuscules, caractères de ponctuation,
    des espaces et des nombres
    """
    if len(sys.argv) < 2:
        print("Entre votre string")
    elif len(sys.argv) > 2:
        print("AssertionError: le nombre des arguments est supereur a un")
        sys.exit(1)
    else:
        nb_punctuation = sum(1 for c in sys.argv[1] if c in string.punctuation)
        print(f"The text contains {len(sys.argv[1])} characters:")
        print(sum(1 for c in sys.argv[1] if c.isupper()), "upper letters")
        print(sum(1 for c in sys.argv[1] if c.islower()), "lower letters")
        print(nb_punctuation, "punctuation marks")
        print(sum(1 for c in sys.argv[1] if c.isspace()), " spaces")
        print(sum(1 for c in sys.argv[1] if c.isdigit()), " digits")


def main():
    """
    main function
    """
    building_print()


if __name__ == "__main__":
    main()
