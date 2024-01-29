import os
import logging

logging.basicConfig(level=logging.INFO)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    folder_name = 'test_folder'
    create_directory(folder_name)

    try:
        # Получаем список файлов в текущей директории
        files = os.listdir(folder_name)

        # Фильтруем только нужные файлы с указанным расширением
        filtered_files = [file for file in files if file.endswith(source_ext)]

        # Сортируем файлы по имени
        filtered_files.sort()

        # Задаем начальный номер для порядкового номера
        num = 1

        # Переименовываем файлы
        for file in filtered_files:
            # Получаем имя файла без расширения
            name = os.path.splitext(file)[0]

            # Если задан диапазон, обрезаем имя файла
            if name_range:
                name = name[name_range[0]-1:name_range[1]]

            # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
            new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

            # Переименовываем файл
            path_old = os.path.join(os.getcwd(), folder_name, file)
            path_new = os.path.join(os.getcwd(), folder_name, new_name)
            os.rename(path_old, path_new)

            # Увеличиваем порядковый номер
            num += 1

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise  # Пробрасываем исключение дальше

# Пример использования
try:
    rename_files("new_file", 3, ".txt", "csv", name_range=(1, 5))
    logging.info("File renaming completed successfully.")
except Exception as e:
    logging.error(f"File renaming failed: {e}")

def run_tests():
    """
    >>> # Подготовка тестовых данных
    >>> create_directory('test_folder')
    >>> open(os.path.join('test_folder', 'file1.txt'), 'a').close()
    >>> open(os.path.join('test_folder', 'file2.txt'), 'a').close()
    >>> open(os.path.join('test_folder', 'file3.txt'), 'a').close()

    >>> # Выполнение тестов
    >>> rename_files("new_file", 3, ".txt", "csv", name_range=(1, 3))
    >>> os.listdir('test_folder')
    ['new_file001.csv', 'new_file002.csv', 'new_file003.csv']
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()

