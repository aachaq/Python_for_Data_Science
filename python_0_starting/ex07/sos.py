import sys


def is_alnum_or_space(s):
    """
    fonction return vrai si la chaîne contient uniquement
    alphanumérique ou des espaces si non return faux.
    """
    return all(char.isalnum() or char.isspace() for char in s)


def is_bad_arguments():
    """
    la fonction qui vérifie si les arguments est correct.
    """
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if not is_alnum_or_space(sys.argv[1]):
        print("AssertionError: the arguments are bad")
        sys.exit(1)


def to_morse(text, morse_dict):
    """
    une fonction convertit la chaîne vers code morse
    se form de list, et se join avec un espace pendent
    la transmition vers une string.
    """
    result = []
    for char in text.upper():
        if char in morse_dict:
            result.append(morse_dict[char])
        else:
            result.append('?')
    return ' '.join(result)


def string_to_morse_code():
    """
    la fonction qui utilise un dictionnaire pour
    transformer la chaine vers un code morse et se afficher.
    """
    morse_dect = {' ': '/', 'A': '.-',
                  'B': '-...', 'C':   '-.-.',
                  'D': '-..',    'E': '.',      'F': '..-.',
                  'G': '--.',    'H': '....',   'I': '..',
                  'J': '.---',   'K': '-.-',    'L': '.-..',
                  'M': '--',     'N': '-.',     'O': '---',
                  'P': '.--.',   'Q': '--.-',   'R': '.-.',
                  'S': '...',    'T': '-',      'U': '..-',
                  'V': '...-',   'W': '.--',    'X': '-..-',
                  'Y': '-.--',   'Z': '--..',

                  '0': '-----',  '1': '.----',  '2': '..---',
                  '3': '...--',  '4': '....-',  '5': '.....',
                  '6': '-....',  '7': '--...',  '8': '---..',
                  '9': '----.'
                  }
    print(to_morse(sys.argv[1], morse_dect))


def main():
    """
    main function
    """
    is_bad_arguments()
    string_to_morse_code()


if __name__ == "__main__":
    main()
