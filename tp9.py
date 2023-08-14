import unittest
from tp7conception import Fraction

class FractionTestCase(unittest.TestCase):
    # ... (previous test methods)

    def test_numerator_and_denominator(self):
        """Test numerator and denominator properties."""
        f = Fraction(3, 5)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 5)

        f.numerator = 7
        f.denominator = 9
        self.assertEqual(f.numerator, 7)
        self.assertEqual(f.denominator, 9)

    def test_string_representation(self):
        """Test string representation of fractions."""
        f = Fraction(5, 6)
        self.assertEqual(str(f), "5/6")

    def test_add(self):
        """Test addition of fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = Fraction(12, 23)
        result = f1 + f2
        result_2 = f1 + f3
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)
        self.assertEqual(result_2.numerator, 47)
        self.assertEqual(result_2.denominator, 46)

    def test_subtract(self):
        """Test subtraction of fractions."""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        result = f1 - f2
        result_2 = f2 - f1
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 8)
        self.assertEqual(result_2.numerator, -2)
        self.assertEqual(result_2.denominator, 8)

    def test_multiplication(self):
        """Test multiplication of fractions."""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        f3 = Fraction(0,12)
        result = f1 * f2
        result_2 = f1 * f3
        self.assertEqual(result.numerator, 6)
        self.assertEqual(result.denominator, 12)
        self.assertEqual(result_2.numerator, 0)
        self.assertEqual(result_2.denominator, 3)

    def test_division(self):
        """Test division of fractions."""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        f3 = Fraction(0,12)
        result = f1 / f2
        self.assertEqual(result.numerator, 8)
        self.assertEqual(result.denominator, 9)
        self.assertRaises(ValueError, f2.__truediv__, f3)


    def test_power(self):
        """Test exponentiation of fractions."""
        f = Fraction(3, 5)
        result = f ** 3
        self.assertEqual(result.numerator, 27)
        self.assertEqual(result.denominator, 125)
        self.assertEqual(f.__pow__(0), 1, "f.Pow(0)")
    
    def test_equality_operator(self):
        """Test the equality operator (__eq__) of fractions."""
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 6)
        self.assertEqual(f1, f2)
        f3 = Fraction(1, 2)
        self.assertNotEqual(f1, f3)

    def test_float_conversion(self):
        """Test conversion of a fraction to a floating-point number."""
        f = Fraction(3, 8)
        self.assertAlmostEqual(float(f), 0.375)

    def test_mixed_number_representation(self):
        """Test mixed number representation of fractions."""
        f = Fraction(8, 3)
        self.assertEqual(f.as_mixed_number(), "2 + 2/3")
        d = Fraction(9, 3)
        self.assertEqual(d.as_mixed_number(), "3")
        e = Fraction(0, 3)
        self.assertEqual(e.as_mixed_number(), "0")

    def test_is_zero(self):
        """Test if a fraction is zero."""
        f = Fraction(0, 7)
        self.assertTrue(f.is_zero())
        f = Fraction(5, 7)
        self.assertFalse(f.is_zero())

    def test_is_integer(self):
        """Test if a fraction is an integer."""
        f1 = Fraction(6, 3)
        self.assertTrue(f1.is_integer())
        f2 = Fraction(5, 2)
        self.assertFalse(f2.is_integer())

    def test_is_proper(self):
        """Test if a fraction is proper."""
        f1 = Fraction(2, 3)
        self.assertTrue(f1.is_proper())
        f2 = Fraction(7, 4)
        self.assertFalse(f2.is_proper())

    def test_is_unit(self):
        """Test if a fraction is a unit fraction."""
        f1 = Fraction(1, 5)
        self.assertTrue(f1.is_unit())
        f2 = Fraction(4, 5)
        self.assertFalse(f2.is_unit())
    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)