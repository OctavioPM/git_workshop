import pytest

import os, sys
from pathlib import Path

main_folder = str(Path.cwd().parent)
sys.path.append(main_folder)

from tutorial.greeting import greet

def test_greet() -> None:
    assert greet("Alice") == "Hello Alice!"
    assert greet("Bob") == "Hello Bob!"
    if greet() != "Hello World!":
        pytest.fail()


if __name__ == "__main__":
    test_greet()