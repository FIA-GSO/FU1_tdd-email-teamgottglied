import re  # regular Expressions
from re import Match
from typing import Optional

def is_valid_email_prefix(prefix: str) -> bool:
    allowed_special_chars = r'^\.!#$%&\'*+-/=\?^_`{|}~$'

    if prefix.startswith('.'):
        return False

    is_valid = True
    for character in prefix:
        is_valid = is_valid and (character.isalpha() or character.isalnum() or re.match(allowed_special_chars, prefix))

    return is_valid


def is_valid_email_suffix(suffix: str) -> Optional[Match[str]]:
    domain_pattern = r'^[\w\.-]+\.\w+$'

    return re.match(domain_pattern, suffix)


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    if email.count('@') != 1:
        return False

    split_email = email.split('@')
    prefix = split_email[0]
    suffix = split_email[1]

    is_valid_mail_prefix = is_valid_email_prefix(prefix)

    if not is_valid_mail_prefix:
        return False

    is_valid_mail_suffix = is_valid_email_suffix(suffix)

    if not is_valid_mail_suffix:
        return False

    return True


print(is_valid_email("hallo@world"))
