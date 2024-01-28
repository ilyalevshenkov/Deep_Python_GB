import os
import logging
import unittest
from your_module_name import create_directory, rename_files  # Замените 'your_module_name' на имя вашего модуля

class TestRenameFiles(unittest.TestCase):

    def setUp(self):
        self.folder_name = 'test_folder'
        create_directory(self.folder_name)

    def tearDown(self):
        # Удаляем временную директорию после каждого теста
        os.rmdir(self.folder_name)

    def test_rename_files_success(self):
        # Создаем тестовые файлы в директории
        file_names = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in file_names:
            file_path = os.path.join(self.folder_name, file_name)
            open(file_path, 'w').close()

        # Переименовываем файлы
        rename_files('new_file', 3, '.txt', 'csv', name_range=(1, 5))

        # Проверяем, что файлы успешно переименованы
        new_file_names = ['new_file001.csv', 'new_file002.csv', 'new_file003.csv']
        for new_name in new_file_names:
            new_path = os.path.join(self.folder_name, new_name)
            self.assertTrue(os.path.exists(new_path))

    def test_rename_files_with_name_range(self):
        # Создаем тестовые файлы в директории
        file_names = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in file_names:
            file_path = os.path.join(self.folder_name, file_name)
            open(file_path, 'w').close()

        # Переименовываем файлы с заданным диапазоном
        rename_files('new_file', 3, '.txt', 'csv', name_range=(2, 3))

        # Проверяем, что только часть файлов успешно переименована
        new_file_names = ['new_file002.csv', 'new_file003.csv']
        for new_name in new_file_names:
            new_path = os.path.join(self.folder_name, new_name)
            self.assertTrue(os.path.exists(new_path))

        # Проверяем, что остальные файлы остались без изменений
        unchanged_file_names = ['file1.txt']
        for unchanged_name in unchanged_file_names:
            unchanged_path = os.path.join(self.folder_name, unchanged_name)
            self.assertTrue(os.path.exists(unchanged_path))

    def test_rename_files_invalid_extension(self):
        # Создаем тестовые файлы в директории с неверным расширением
        file_names = ['file1.jpg', 'file2.jpg', 'file3.jpg']
        for file_name in file_names:
            file_path = os.path.join(self.folder_name, file_name)
            open(file_path, 'w').close()

        # Переименовываем файлы
        with self.assertRaises(ValueError):
            rename_files('new_file', 3, '.txt', 'csv')

        # Проверяем, что файлы не были переименованы
        for original_name in file_names:
            original_path = os.path.join(self.folder_name, original_name)
            self.assertTrue(os.path.exists(original_path))

    def test_rename_files_directory_does_not_exist(self):
        # Удаляем текущую директорию
        os.rmdir(self.folder_name)

        # Переименовываем файлы в несуществующей директории
        with self.assertRaises(Exception) as context:
            rename_files('new_file', 3, '.txt', 'csv')

        self.assertIn('No such file or directory', str(context.exception))

    def test_rename_files_invalid_name_range(self):
        # Создаем тестовые файлы в директории
        file_names = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in file_names:
            file_path = os.path.join(self.folder_name, file_name)
            open(file_path, 'w').close()

        # Переименовываем файлы с неверным диапазоном
        with self.assertRaises(ValueError):
            rename_files('new_file', 3, '.txt', 'csv', name_range=(4, 5))

        # Проверяем, что файлы не были переименованы
        for original_name in file_names:
            original_path = os.path.join(self.folder_name, original_name)
            self.assertTrue(os.path.exists(original_path))

if __name__ == '__main__':
    unittest.main()
