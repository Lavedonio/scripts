"""
    Generates a secure password based on the requisites given.
"""
import argparse
import secrets
import string


DEFAULT_LENGTH = 20


def main(password_length: int, use_letters: bool = True, use_numbers: bool = True,
         use_special_chars: bool = True):

    assert use_letters or use_numbers or use_special_chars, "Unable to generate password"

    # Adding all available choices
    char_choices = ''

    if use_letters:
        char_choices += string.ascii_letters
    
    if use_numbers:
        char_choices += string.digits
    
    if use_special_chars:
        char_choices += string.punctuation + 'çÇ'

    # Choosing new password
    password = ''.join(secrets.choice(char_choices) for _ in range(password_length))

    try:
        assert not use_letters or any(i in password for i in string.ascii_letters)
        assert not use_numbers or any(i in password for i in string.digits)
        assert not use_special_chars or any(i in password for i in string.punctuation)
    except AssertionError:
        main(password_length, use_letters, use_numbers, use_special_chars)
    else:
        print("Password generated:")
        print(password)


if __name__ == '__main__':
    # For more info run:
    # python password_generator.py --help

    parser = argparse.ArgumentParser(prog="password_generator",
                                     epilog="Created by Daniel Lavedonio de Lima",
                                     description="Generate a secure password based on the requisites given. Defaults to alphanumeric.")
    parser.add_argument('-v', '--version', action='version',
                        version="%(prog)s 1.0.0")
    parser.add_argument('-l', '--letters', dest="use_letters", action='store_true', default=False,
                        help="Add letters.")
    parser.add_argument('-d', '--digits', dest="use_digits", action='store_true', default=False,
                        help="Add digits.")
    parser.add_argument('-s', '--special-chars', dest="use_special_chars", action='store_true', default=False,
                        help="Add special characters.")
    parser.add_argument('length', metavar="LENGTH", type=int, nargs='?', default=DEFAULT_LENGTH,
                        help=f"Password length. Default: {DEFAULT_LENGTH}")

    args = parser.parse_args()

    # If no parameters are given, defaults to an alphanumeric password
    if not (args.use_letters or args.use_digits or args.use_special_chars):
        args.use_letters = True
        args.use_digits = True

    main(args.length, args.use_letters, args.use_digits, args.use_special_chars)
