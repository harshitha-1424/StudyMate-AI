"""
helpers.py

Common helper functions.
"""

from datetime import datetime


def current_timestamp() -> str:
    """
    Returns current timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def execution_time(start, end):
    """
    Returns execution time.
    """

    return round(end - start, 2)


def percentage(part, whole):
    """
    Calculates percentage safely.
    """

    if whole == 0:
        return 0

    return round((part / whole) * 100, 2)