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


"""Ex 2"""
