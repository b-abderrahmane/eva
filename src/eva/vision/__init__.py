"""EVA vision API."""
try:
    pass
except ImportError as e:
    msg = (
        "EVA vision requirements are not installed.\n\n"
        "Please pip install as follows:\n"
        '  python -m pip install "eva[vision]" --upgrade'
    )
    raise ImportError(str(e) + "\n\n" + msg) from e