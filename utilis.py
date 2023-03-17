import os


def clear_console():
    """
    Used to clear the terminal of all text
    """
    os.system("cls" if os.name == "nt" else "clear")
