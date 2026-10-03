# tests/test_validator.py
import pytest

from phone_validator import is_valid_phone


def test_all_valid_fixture_phones(valid_phones):
    for phone in valid_phones:
        assert is_valid_phone(phone) is True, f"должен быть валидным: {phone!r}"


def test_all_invalid_fixture_phones(invalid_phones):
    for phone in invalid_phones:
        assert is_valid_phone(phone) is False, f"должен быть невалидным: {phone!r}"