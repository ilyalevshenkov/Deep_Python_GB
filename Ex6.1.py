#Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

#Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в
# зависимости от результата проверки.


#date_to_prove = '15.4.2023'
#date_to_prove = "31.6.2022"

def is_leap(year: int):
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str):
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2:
        if is_leap(year):
            if date > 29:
                return False
        else:
            if date > 28:
                return False
    elif date < 1 or date > 31:
        return False
    return True

print(valid(date_to_prove))
