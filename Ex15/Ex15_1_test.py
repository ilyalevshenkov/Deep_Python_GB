import unittest

class TestMatrixOperations(unittest.TestCase):

    def test_matrix_addition(self):
        matrix1 = Matrix(2, 3)
        matrix1.data = [[1, 2, 3], [4, 5, 6]]

        matrix2 = Matrix(2, 3)
        matrix2.data = [[7, 8, 9], [10, 11, 12]]

        result_addition = matrix1 + matrix2

        expected_result = Matrix(2, 3)
        expected_result.data = [[8, 10, 12], [14, 16, 18]]

        self.assertEqual(result_addition, expected_result, "Matrix addition test failed.")

    def test_matrix_multiplication(self):
        matrix3 = Matrix(3, 2)
        matrix3.data = [[1, 2], [3, 4], [5, 6]]

        matrix4 = Matrix(2, 4)
        matrix4.data = [[7, 8, 9, 10], [11, 12, 13, 14]]

        result_multiplication = matrix3 * matrix4

        expected_result = Matrix(3, 4)
        expected_result.data = [[29, 32, 35, 38], [65, 72, 79, 86], [101, 112, 123, 134]]

        self.assertEqual(result_multiplication, expected_result, "Matrix multiplication test failed.")

    def test_invalid_addition(self):
        matrix1 = Matrix(2, 3)
        matrix2 = Matrix(3, 2)

        with self.assertRaises(ValueError):
            result = matrix1 + matrix2

    def test_invalid_multiplication(self):
        matrix1 = Matrix(2, 3)
        matrix2 = Matrix(3, 2)

        with self.assertRaises(ValueError):
            result = matrix1 * matrix2

    def test_matrix_equality(self):
        matrix1 = Matrix(2, 3)
        matrix1.data = [[1, 2, 3], [4, 5, 6]]

        matrix2 = Matrix(2, 3)
        matrix2.data = [[1, 2, 3], [4, 5, 6]]

        self.assertEqual(matrix1, matrix2, "Matrix equality test failed.")

if __name__ == '__main__':
    unittest.main()
