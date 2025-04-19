import sys
from ft_filter import ft_filter


def is_bad_arguments():
    """
    la fonction qui test si des arguments incorrect
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if not isinstance(sys.argv[1], str):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if not sys.argv[2].isdigit():
        print("AssertionError: the arguments are bad")
        sys.exit(1)


def string_to_list():
    """
    la fonction qui transfert la string vers list
    """
    list1 = []
    list1 = sys.argv[1].split()
    return list1


def length_greater_than_N():
    """
    la fonction qui return les mots dont un nombre
    de caractere superieur a N
    """
    lst = []
    list_length_greater_than_N = []

    lst = string_to_list()
    list_length_greater_than_N = ft_filter(
        lambda x: len(x) > int(sys.argv[2]), lst)
    print(list(list_length_greater_than_N))


def main():
    """
    main function
    """
    is_bad_arguments()
    length_greater_than_N()


if __name__ == "__main__":
    main()
