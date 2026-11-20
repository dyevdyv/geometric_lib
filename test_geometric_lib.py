import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(circle.area(5), math.pi * 25)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            circle.area(None)
        with self.assertRaises(TypeError):
            circle.perimeter("5")


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square.area(6), 36)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(6), 24)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            square.area(None)
        with self.assertRaises(TypeError):
            square.perimeter(None)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_area_positive(self):
        self.assertEqual(rectangle.area(4, 7), 28)

    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(4, 7), 22)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle.area(None, 5)
        with self.assertRaises(TypeError):
            rectangle.perimeter(5, None)


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_height(self):
        self.assertEqual(triangle.area(10, 0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(triangle.area(10, 5), 25.0)

    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(3.5, 2.0), 3.5)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            triangle.area(None, 5)
        with self.assertRaises(TypeError):
            triangle.perimeter(3, None, 5)


if __name__ == "__main__":
    unittest.main()