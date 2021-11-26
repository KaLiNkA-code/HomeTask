"""
Калинин Егор 9 класс
10.11.21
"""

""" Углубленный
Ex 1
"""
cords = []  # Координаты
total = []  # тут поле
middle_v = []  # тут все центры
gg = []  # тут список всех центров центра
light = []  # тут хранится сила фонаря

h, l = input().split()  # Тут единственный PEP 8, но в контексте плучаемого ввода пофиксить его я не смогу
LC = int(input())

for _ in range(LC):
    val = input()
    a1, a2, a3 = val.split()
    cords.append([int(a1), int(a2), int(a3)])  # Хотел через extend, но все таки нужно как то отделать

total_lend = int(l) * int(h)

for i in range(total_lend):  # Составляем поле (хотел сделать с помощью экземпляров, но оказалось, что это не нужно)
    total.append(False)

print(cords)
for j1 in cords:  # берем индекс координаты точки, на которой лежит фонарь
    a = j1[1] * int(l) + j1[0] + 1
    middle_v.append(a)
    light.append(j1[2])

for i in range(len(middle_v)):  # вот этот фрагмент кода я затрудняюсь сделать для всех случаев жизни :/
    g = []
    if int(l) <= middle_v[i]:
        val1 = middle_v[i] - int(l)
        g.append(val1)
    val2 = middle_v[i]
    g.append(val2)
    if int(l) + middle_v[i] <= len(total):
        val3 = middle_v[i] + int(l)
        g.append(val3)
    gg.append(g)

print(gg)

light_val = 0
c = 0  # Индекс фонаря
for i in gg:  # Нужен для того, чтобы откидывать лучши от существующих значений
    light_val = i[c]
    for j in i:
        while light_val != 0:
            print(light_val)
            light_val -= 1

    c += 1

c = 0
print(middle_v)


import csv
import matplotlib.pyplot as plt
# import pandas as pd
string = input()
index = 0
new_string = []

for j in string:
    for i in j:
        if i in '!?.,-':
            new_string.append(i)
            new_string.append(' ')
        elif i == ' ' and not new_string[-1] == ' ':
            new_string.append(i)
        elif index > 2:
            if new_string[-1] == ' ' and new_string[-2] in '!?.':
                new_string.append(i.upper())
            elif i != ' ':
                new_string.append(i)
    index += 1

print(''.join(new_string))


for j in string:
    for i in j:
        if i in '!?.,-':
            new_string += i
            new_string += ' '
        elif i == ' ' and not new_string[-1] == ' ':
            new_string += i
        elif i != ' ':
            new_string += i
    index += 1

print(new_string)

"""номер 3 не знаю, что нужно от меня делать"""

"""Доп задания"""

"""Номер 1"""
with open('transactions.csv', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    m1 = m2 = m3 = 0
    for i in reader:
        if i[2] and i[2] == 'OK':
            if int(i[3]) > m1:
                m3 = m2
                m2 = m1
                m1 = int(i[3])
    print(f"{m1}, {m2}, {m3}")

"""Номер 2"""

with open('transactions.csv', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    result = 0
    for i in reader:
        if i[2] and i[2] == 'OK':
            result += int(i[3])
    print(result)


"""Номер 3"""


with open('flights.csv', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    name = []
    dicct = {}
    for i in reader:

        if i[1] not in dicct:
            dicct.update({i[1]: [0, 0, 0, [], [], []]})
        else:
            dicct[i[1]][0] += 1
            dicct[i[1]][3].append(dicct[i[1]][0] + 1)
            dicct[i[1]][1] += int(i[2])
            dicct[i[1]][4].append(int(i[2]))
            dicct[i[1]][2] += int(i[3])
            dicct[i[1]][5].append(int(i[3]))
    # Полная стоимость

    for k, v in dicct.items():
        print(f"Комапания {k} сделала {v[0]} перелетов, стоимость: {v[1]}, а общий вес: {v[2]}.")
        fig, ax = plt.subplots()
        ax.plot(linewidth=3)
        ax.set_title(f"График {k}", fontsize=24)
        ax.set_ylabel('Value', fontsize=14)
        ax.set_xlabel('Number', fontsize=14)
        ax.tick_params(axis='both', labelsize=14)
        ax.plot(v[4], c='red')
        plt.plot(v[5], c='green')
        plt.plot(v[3], c='blue')
        plt.show()
