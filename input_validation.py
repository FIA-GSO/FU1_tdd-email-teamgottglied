import re  # regular Expressions
from re import Match
from typing import Optional

allowed_special_chars = [".", "!", "#", "$", "%", "&", "\\", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{",
                         "|", "}"]


def is_valid_email_prefix(prefix: str) -> bool:
    if prefix.startswith('.'):
        return False

    is_valid = True
    for character in prefix:
        is_valid = (is_valid
                    and (character.isalpha()
                         or character.isalnum()
                         or character in allowed_special_chars))

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


def valid_short_password(password: str):
    has_special = False
    has_number = False
    has_upper = False
    has_lower = False

    for character in password:
        if character in allowed_special_chars:
            has_special = True
        if character.islower():
            has_lower = True
        if character.isupper():
            has_upper = True
        if character.isnumeric():
            has_number = True

    return has_special and has_upper and has_lower and has_number


def valid_long_password(password: str):
    has_special = False
    has_number = False
    has_upper = False
    has_lower = False

    for character in password:
        if character in allowed_special_chars:
            has_special = True
        if character.islower():
            has_lower = True
        if character.isupper():
            has_upper = True
        if character.isnumeric():
            has_number = True

    return (
            (has_special and has_upper)
            or (has_special and has_number)
            or (has_special and has_lower)

            or (has_number and has_upper)
            or (has_number and has_lower)

            or (has_lower and has_lower)
            )


def is_valid_password(password: str) -> bool:
    if type(password) != str:
        raise ValueError

    if len(password) >= 25 and (valid_short_password(password) or valid_long_password(password)):
        return True

    if len(password) >= 8 and valid_short_password(password):
        return True

    return False
