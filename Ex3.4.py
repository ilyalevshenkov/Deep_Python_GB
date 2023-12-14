

duplicates = set()
lst = [1, 2, 2, 3, 4, 4, 5, 5]  # Пример списка lst
for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)

