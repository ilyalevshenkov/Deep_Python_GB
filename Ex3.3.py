#На вход подается словарь со списком вещей для похода в качестве ключа
# и их массой max_weight в качестве значения.
#Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
#В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.
#В переменную result выведите список, содержащий все возможные варианты backpack. Напечатайте переменную result.
#*Верните все возможные варианты комплектации рюкзака.

backpacks = []
max_weight = 1.0  # Замените на максимальный вес
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
for i in range(2**len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)
full_result = [backpack for backpack in backpacks if backpack]
result = []
for item in full_result:
    if item not in result:
        result.append(item)

# Форматируем и выводим результат
result = '[' + ',\n'.join(map(str, result)) + ']'
print(result)

