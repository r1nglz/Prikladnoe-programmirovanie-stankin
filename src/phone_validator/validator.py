# src/phone_validator/validator.py

import re


_PHONE_RE = re.compile(
    r"^"
    r"\+?"                           # Опциональный знак '+' в начале
    r"(?:\d[\s\-\(\)]*){7,15}"       # От 7 до 15 цифр (стандарт E.164), между которыми могут быть пробелы, дефисы и скобки
    r"$"
)


def is_valid_phone(phone: str) -> bool:
    """Проверяет, является ли строка синтаксически корректным номером телефона.

    Args:
        phone: строка для проверки.

    Returns:
        True, если номер телефона похож на корректный, иначе False.

    Examples:
        >>> is_valid_phone("+7 (999) 123-45-67")
        True
        >>> is_valid_phone("89991234567")
        True
        >>> is_valid_phone("not-a-phone")
        False
    """
    if not isinstance(phone, str):
        return False
    if not phone or len(phone) > 30:
        return False
    return _PHONE_RE.match(phone) is not None