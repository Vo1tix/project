import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from history import HalfHistory, OneHistory


class TestHalfHistory(unittest.TestCase):
    def test_empty(self):
        h = HalfHistory(3)
        self.assertEqual(h.get_actions(), [])
        self.assertEqual(len(h), 0)

    def test_less_than_capacity(self):
        h = HalfHistory(5)
        for x in [1, 2, 3]:
            h.add(x)
        self.assertEqual(h.get_actions(), [1, 2, 3])

    def test_exact_capacity(self):
        h = HalfHistory(3)
        for x in [1, 2, 3]:
            h.add(x)
        self.assertEqual(h.get_actions(), [1, 2, 3])

    def test_overflow_discard_half(self):
        h = HalfHistory(4)
        for x in [1, 2, 3, 4]:
            h.add(x)

        h.add(5)
        self.assertEqual(h.get_actions(), [3, 4, 5])

        h.add(6)
        self.assertEqual(h.get_actions(), [3, 4, 5, 6])

        h.add(7)
        self.assertEqual(h.get_actions(), [5, 6, 7])

    def test_capacity_one(self):
        h = HalfHistory(1)
        h.add(1)
        self.assertEqual(h.get_actions(), [1])
        h.add(2)
        self.assertEqual(h.get_actions(), [2])

    def test_duplicates(self):
        h = HalfHistory(3)
        for x in [1, 1, 1, 1]:
            h.add(x)
        self.assertEqual(h.get_actions(), [1, 1])

    def test_len_never_exceeds_capacity(self):
        h = HalfHistory(5)
        for i in range(100):
            h.add(i)
            self.assertLessEqual(len(h), 5)

    def test_order_is_kept(self):
        h = HalfHistory(6)
        for i in range(10):
            h.add(i)
        self.assertEqual(h.get_actions(), [6, 7, 8, 9])

    def test_copies_counter(self):
        h = HalfHistory(4)
        for x in range(4):
            h.add(x)
        self.assertEqual(h.copies, 0)

        h.add(4)
        self.assertEqual(h.copies, 2)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            HalfHistory(0)


class TestOneHistory(unittest.TestCase):
    def test_overflow_discard_one(self):
        h = OneHistory(3)
        for x in [1, 2, 3]:
            h.add(x)

        h.add(4)
        self.assertEqual(h.get_actions(), [2, 3, 4])

        h.add(5)
        self.assertEqual(h.get_actions(), [3, 4, 5])

    def test_capacity_one(self):
        h = OneHistory(1)
        h.add(1)
        self.assertEqual(h.get_actions(), [1])
        h.add(2)
        self.assertEqual(h.get_actions(), [2])

    def test_len_never_exceeds_capacity(self):
        h = OneHistory(4)
        for i in range(50):
            h.add(i)
            self.assertLessEqual(len(h), 4)

    def test_copies_counter(self):
        h = OneHistory(3)
        for x in [1, 2, 3]:
            h.add(x)
        self.assertEqual(h.copies, 0)

        h.add(4)
        self.assertEqual(h.copies, 2)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            OneHistory(-1)


if __name__ == "__main__":
    unittest.main()