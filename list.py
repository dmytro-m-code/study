name = 'Ivan'
names = ['Ivan', 'Peter', 'Tom']
list1 = ['something', 4, 5]
my_list = list(name) # функции, переменные
list2 = [12, 14, 34]



list_all = list1 + list2

# Добавление элементов

list2.append(55)
list2.append([30, 40, 50]) # Добавить элемент в конец списка
list2.insert(0, 20) # Добавить элемент в определённую позицию
list2.extend([30, 40, 50]) # Добавить несколько элементов в конец списка

# Удаление элементов

list2.remove(30) # Удалить первый найденный элемент по значению
deleted = list2.pop(1) # Удалить элемент по индексу и вернуть его 
list2.clear() # Очистить весь список 

# Сортировка
list2.sort()
sorted_lst = sorted(list2)
sorted_lst = sorted(names, key=len)
sorted_lst = sorted(list2)


exists = 10 in list2


print(sorted_lst)

for name in names:
    print(name)

for index in range(len(names)):
    print(f'Index {index}: {names[index]}')

for index, value in enumerate(names):
    print(f"Index {index}: {value}")

for num in names[::2]: # Каждый второй элемент 
	print(num)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")