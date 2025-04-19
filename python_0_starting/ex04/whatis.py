import sys

def is_negative_digit(str) -> bool:
    if str.startswith("-") and str[1:].isdigit():
        return True
    else:
        False

    

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)

if len(sys.argv) < 2:
    sys.exit(1)



argv = ""
if (sys.argv[1].isdigit() or is_negative_digit(sys.argv[1]) == True):
    argv = int(sys.argv[1])

if isinstance(argv, int) == True:
    if argv % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    print("AssertionError: argument is not an integer")
    sys.exit(1)
