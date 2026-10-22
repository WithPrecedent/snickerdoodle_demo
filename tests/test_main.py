"""Main file for unit tests."""

from __future__ import annotations

import snickerdoodle_demo


def test_snickerdoodle_demo() -> None:
    assert snickerdoodle_demo.__version__ == '0.0.1'

if __name__ == '__main__':
    test_snickerdoodle_demo()
