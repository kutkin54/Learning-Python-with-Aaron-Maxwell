from unittest import TestCase
from splitting import split_amount


class TestSplitting(TestCase):
    def test_splitting_amount(self):
        self.assertEqual([1], split_amount(1, 1))
        self.assertEqual([2, 2], split_amount(4, 2))
        self.assertEqual([2, 3, 1], split_amount(5, 3))
