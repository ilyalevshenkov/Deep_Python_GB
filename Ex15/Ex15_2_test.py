# HW11_3

import unittest

class TestRectangleMethods(unittest.TestCase):

    def test_perimeter(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.perimeter(), 14)

    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_addition(self):
        rect1 = Rectangle(3, 4)
        rect2 = Rectangle(5, 5)
        result = rect1 + rect2
        self.assertEqual(result.width, 8)
        self.assertEqual(result.height, 6)

    def test_subtraction(self):
        rect1 = Rectangle(3, 4)
        rect2 = Rectangle(1, 1)
        result = rect1 - rect2
        self.assertEqual(result.width, 2)
        self.assertEqual(result.height, 2)

    def test_comparison(self):
        rect1 = Rectangle(3, 4)
        rect2 = Rectangle(5, 5)
        self.assertTrue(rect1 < rect2)
        self.assertFalse(rect1 == rect2)
        self.assertTrue(rect1 <= rect2)

if __name__ == '__main__':
    unittest.main()
