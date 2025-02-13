# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# # написать по 5 проверок по аналогии кода выше

# car = 'lamba'
# print("Is car == 'lamba'? I predict True.")
# print(car == 'lamba')

# print("\nIs car == 'ferrary'? I predict False.")
# print(car == 'ferrary')

# car = 'toyota'
# print("Is car == 'toyota'? I predict True.")
# print(car == 'toyota')

# print("\nIs car == 'skoda'? I predict False.")
# print(car == 'skoda')

# car = 'opel'
# print("Is car == 'opel'? I predict True.")
# print(car == 'opel')

# print("\nIs car == 'dodge'? I predict False.")
# print(car == 'dodge')

# car = 'ford'
# print("Is car == 'ford'? I predict True.")
# print(car == 'ford')

# print("\nIs car == 'linkoln'? I predict False.")
# print(car == 'linkoln')


# задать инопланетянена, создать переменную color. Записать зеленый желтый красный цвета. 
# 	- если мы сбили зеленого пришельца, то вывести сообщение что мы заработали 5 балов
# 	- написать контрукцию, если пришелец зелетый, то 5 балов, желтый - 10, красный 15
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
	print('You have 5 points')
if 'yellow' in alien_color:
	print('You have 10 points for yellow')
if 'red' in alien_color:
	print('You have 15 points for red')


if 'green' in alien_color:
	print('You have 5 points')
if 'yellow' in alien_color:
	print('You have 10 points')
if 'red' in alien_color:
	print('You have 15 points')

# написать конструкцию if else, которая определяет в какой фазе жизни находится человек
#  - если меньше двух лет, то немовля
#  - от 2 до 4 - малюк
#  - от 4 до 13 - дитина
#  - от 13 до 20 - подросток
#  - от 20 до 65 - взрослый
#  - больше 65 - старик

	age = 66
if age < 2:
	print('Its a namovlya')
elif 2 <= age < 4:
	print('Its malyuk')
elif 4 <= age < 13:
	print('Its ditina')
elif 13 <= age < 20:
	print('Its pidlitok')
elif 20 <= age < 65:
	print('Its doroslyi')
else:
	print('Its starik')

# составить список 3 фруктов
# написать 5 операторов if else, если фрукт в списке то вывести you really like bananas!


favourite_fruits = ['apple', 'orange', 'kiwi']

if 'apple' in favourite_fruits:
	print('I really like apple')
if 'orange' in favourite_fruits:
	print('I really like orange')
if 'banana' in favourite_fruits:
	print('I dont like banana')
if 'kiwi' in favourite_fruits:
	print('I really like kiwi')
if 'pineapple' in favourite_fruits:
	print('I dont like pineapple')


# сделать список из 5 пользователей включительно с админом
# пройтись циклом по списку

# если имя админ, то вывести особенное сообщение, в других случаях вывести сообщение привтствия
# - добавить оператор if который проверяет не пуст ли список
# создать два списка, если есть повторяющиеся пользователи, то вывести сообщение про это
# если нету, то указать что пользователь свободный

current_users = ['Admin', 'Bob', 'User1', 'Test', 'Login']
current_users = ['admin', 'bob', 'user1', 'test', 'login']
new_users = ['admin', 'jack', 'user1', 'dinal', 'alberto']

for new_user in new_users:
 	if new_user in current_users:
 		print(f"login {new_user} aleady exist")
 	else:
 		print(f"login {new_user} is free")

print("\nWelcome")

# последовательные числители указывают на позицию в списке - первый, второй...
# - сохранить числа от 1 до 9 в список
# - пройтись циклом по списку
# - при помощи if else вывести правильные окончания для каждого числа

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}td")
    elif number == 4:
        print(f"{number}th")
    elif number == 5:
        print(f"{number}th")
    elif number == 6:
        print(f"{number}th")
    elif number == 7:
        print(f"{number}th")
    elif number == 8:
        print(f"{number}th")
    elif number == 9:
        print(f"{number}nd")
