# -*- coding: utf-8 -*-

from .context import sample

import unittest


class TestCase(unittest.TestCase):
    """Test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()