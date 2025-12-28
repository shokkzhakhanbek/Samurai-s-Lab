import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import add

def test_add():
    assert add(1, 2) == 3
