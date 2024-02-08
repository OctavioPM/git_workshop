from typing import Optional


def greet(username: Optional[str] = None) -> str:
    """Greet a given user.

    When no user is given, this function will return "Hello World!".

    parameters
    ----------
    username: Optional[str]
        Name of the user.

    returns
    -------
    str
        Personalized greeting.
    """
    username = "World" if username is None else username
    return f"Hello {username}!"
