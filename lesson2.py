#Задание 1

my_list = [12, None, -77, 'True', True, 9.5]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)

#Задание 2

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

#Задание 3

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")

#Задание 4

my_str = input("введите несколько слов через пробел: ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1


#Задание 5

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
my_el = int(input("Введите число: "))


    for el in range(len(my_list)):
        if my_list[el] == my_el:
            my_list.insert(el + 1, digit)
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    
#Задание 6

index  = 1
result = []
spec = ["название", "цена", "количество", "единица"]

while True:
    quest = input("Добавить новый товар да/нет?")
    if quest.upper()=="НЕТ"
        break
    item = {}


    for i in spec:
        user_data = input(f"Введите {i}")
        if user_data.isdigit():
            item[i] = int(user_data)
        else:
            item[i] = user_data
    
    result.append(tuple([index, item]))
    index += 1

print(result)


