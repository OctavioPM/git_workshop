import os, sys
from pathlib import Path

main_folder = str(Path.cwd().parent)
sys.path.append(main_folder)

import pytest

from tutorial.greeting import greet


print("Fine")