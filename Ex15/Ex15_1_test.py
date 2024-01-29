import itertools
import logging
import argparse

# Настройка базового уровня логирования
logging.basicConfig(level=logging.INFO)

class Matrix:
    def __init__(self, rows, cols, data=None):
        """
        Конструктор класса Matrix.

        Parameters:
        - rows (int): Количество строк в матрице.
        - cols (int): Количество столбцов в матрице.
        - data (list, optional): Двумерный список данных матрицы. По умолчанию None.
        """
        self.rows = rows
        self.cols = cols
        self.data = data or [[0 for _ in range(cols)] for _ in range(rows)]
        logging.info(f"Создана матрица {self}")

    def __str__(self):
        """
        Возвращает строковое представление матрицы.
        """
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __repr__(self):
        """
        Возвращает строковое представление объекта Matrix.
        """
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        """
        Проверяет равенство матриц.
        """
        return self.data == other.data

    def __add__(self, other):
        """
        Выполняет сложение матриц.

        Parameters:
        - other (Matrix): Другая матрица для сложения.

        Returns:
        - Matrix: Результат сложения матриц.
        """
        if self.rows != other.rows or self.cols != other.cols:
            logging.error("Matrix dimensions do not match for addition.")
            raise ValueError("Matrices have different dimensions!")
        result = Matrix(self.rows, self.cols)
        for i, j in itertools.product(range(self.rows), range(self.cols)):
            result.data[i][j] = self.data[i][j] + other.data[i][j]
        logging.info(f"Выполнено сложение матриц: {self} + {other} = {result}")
        return result

    def __sub__(self, other):
        """
        Выполняет вычитание матриц.

        Parameters:
        - other (Matrix): Другая матрица для вычитания.

        Returns:
        - Matrix: Результат вычитания матриц.
        """
        if self.rows != other.rows or self.cols != other.cols:
            logging.error("Matrix dimensions do not match for subtraction.")
            raise ValueError("Matrices have different dimensions!")
        result = Matrix(self.rows, self.cols)
        for i, j in itertools.product(range(self.rows), range(self.cols)):
            result.data[i][j] = self.data[i][j] - other.data[i][j]
        logging.info(f"Выполнено вычитание матриц: {self} - {other} = {result}")
        return result

    def __mul__(self, other):
        """
        Выполняет умножение матриц.

        Parameters:
        - other (Matrix): Другая матрица для умножения.

        Returns:
        - Matrix: Результат умножения матриц.
        """
        if self.cols != other.rows:
            logging.error(
                "Number of columns in the first matrix is not equal to the number of rows in the second matrix."
            )
            raise ValueError(
                "Number of columns in the first matrix is not equal to the number of rows in the second matrix!"
            )
        result = Matrix(self.rows, other.cols)
        for i, j in itertools.product(range(self.rows), range(other.cols)):
            for k in range(self.cols):
                result.data[i][j] += self.data[i][k] * other.data[k][j]
        logging.info(f"Выполнено умножение матриц: {self} * {other} = {result}")
        return result

    def __truediv__(self, scalar):
        """
        Выполняет деление матрицы на скаляр.

        Parameters:
        - scalar (int or float): Скалярный делитель.

        Returns:
        - Matrix: Результат деления матрицы на скаляр.
        """
        if scalar == 0:
            logging.error("Cannot divide by zero.")
            raise ValueError("Cannot divide by zero!")
        result = Matrix(self.rows, self.cols)
        for i, j in itertools.product(range(self.rows), range(self.cols)):
            result.data[i][j] = self.data[i][j] / scalar
        logging.info(f"Выполнено деление матрицы на скаляр: {self} / {scalar} = {result}")
        return result

def main():
    # Определение параметров командной строки
    parser = argparse.ArgumentParser(description="Matrix Operations")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Matrix operation to perform")
    parser.add_argument("matrix1_rows", type=int, help="Number of rows in the first matrix")
    parser.add_argument("matrix1_cols", type=int, help="Number of columns in the first matrix")
    parser.add_argument("matrix2_rows", type=int, help="Number of rows in the second matrix")
    parser.add_argument("matrix2_cols", type=int, help="Number of columns in the second matrix")
    parser.add_argument("--scalar", type=float, help="Scalar value for division operation")

    args = parser.parse_args()

    # Создание матриц
    matrix1 = Matrix(args.matrix1_rows, args.matrix1_cols)
    matrix2 = Matrix(args.matrix2_rows, args.matrix2_cols)

    # Выполнение выбранной операции
    if args.operation == "add":
        try:
            result = matrix1 + matrix2
            print("Результат сложения:")
            print(result)
        except ValueError as e:
            print(f"Ошибка: {e}")
            logging.error(f"Ошибка при выполнении сложения матриц: {e}")
    elif args.operation == "subtract":
        try:
            result = matrix1 - matrix2
            print("Результат вычитания:")
            print(result)
        except ValueError as e:
            print(f"Ошибка: {e}")
            logging.error(f"Ошибка при выполнении вычитания матриц: {e}")
    elif args.operation == "multiply":
        try:
            result = matrix1 * matrix2
            print("Результат умножения:")
            print(result)
        except ValueError as e:
            print(f"Ошибка: {e}")
            logging.error(f"Ошибка при выполнении умножения матриц: {e}")
    elif args.operation == "divide":
        try:
            result = matrix1 / args.scalar
            print("Результат деления:")
            print(result)
        except ValueError as e:
            print(f"Ошибка: {e}")
            logging.error(f"Ошибка при выполнении деления матрицы на скаляр: {e}")

if __name__ == "__main__":
    # Примеры использования класса Matrix
    # Пример 1: Сложение матриц
    """
    >>> matrix1 = Matrix(2, 3, data=[[1, 2, 3], [4, 5, 6]])
    >>> matrix2 = Matrix(2, 3, data=[[7, 8, 9], [10, 11, 12]])
    >>> result = matrix1 + matrix2
    >>> print(result)
    8 10 12
    14 16 18
    """

    # Пример 2: Вычитание матриц
    """
    >>> matrix3 = Matrix(2, 2, data=[[5, 8], [2, 6]])
    >>> matrix4 = Matrix(2, 2, data=[[1, 3], [4, 2]])
    >>> result = matrix3 - matrix4
    >>> print(result)
    4 5
    -2 4
    """

    # Пример 3: Умножение матриц
    """
    >>> matrix5 = Matrix(3, 2, data=[[1, 2], [3, 4], [5, 6]])
    >>> matrix6 = Matrix(2, 3, data=[[7, 8, 9], [10, 11, 12]])
    >>> result = matrix5 * matrix6
    >>> print(result)
    27 30 33
    61 68 75
    95 106 117
    """

    # Пример 4: Деление матрицы на скаляр
    """
    >>> matrix7 = Matrix(2, 2, data=[[6, 9], [12, 15]])
    >>> result = matrix7 / 3
    >>> print(result)
    2.0 3.0
    4.0 5.0
    """

    # Запуск тестов с использованием doctest
    import doctest
    doctest.testmod()



