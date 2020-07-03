"""
In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit.
Input: A string.

Output: A bool.
"""

import re


def is_acceptable_password(password: str) -> bool:
    search_num = re.search(r'\d', password)
    search_char = re.search(r'\D', password)
    return False if not search_num or not search_char else len(password) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('shorsdt1'))
    
