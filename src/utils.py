"""Shared display helpers."""

DIVIDER = "-" * 60


def print_response(provider: str, text: str) -> None:
    print(f"\n{DIVIDER}")
    print(f"  {provider}")
    print(DIVIDER)
    print(text.strip())
