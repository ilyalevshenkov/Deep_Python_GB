
# Введите ваше решение ниже
num = 2
if num < 1 or num > 100000 or num < 2:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} является простым числом")
    else:
        print(f"{num} является составным числом")

# Идеальное решение GB
if num <= 1 or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "является простым числом")
    else:
        print(num, "является составным числом")
