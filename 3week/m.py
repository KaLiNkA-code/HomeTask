light_info = []  # Список координат
area = []  # список всех ячеек
middle_light = []  # тут у нас центры
light_power = []  # мощность света
middle_list = []  # список центральной оси


h, l = input().split()
LC = int(input())
for _ in range(LC):
    val = input()
    a1, a2, a3 = val.split()
    light_info.append([int(a1), int(a2), int(a3)])


print(f"light info - {light_info} тут мы добавили информацию о координатах и мощности фонарей")

for i in range(int(h) * int(l)):  # Делаем ячейки
    area.append(False)

print(f"len area: {len(area)}")
print(f"area: {area}")

for val in light_info:
    middle_light.append(val[1] * int(l) + val[0] + 1)
    light_power.append(val[2])

print(f"middle_light: {middle_light}")
print(f"light_power{light_power}")

c = 0  # индекс light info (центра фонаря)
_t = 0
for i in middle_light:  # i = центр
    val = int(l)  # тут у нас ширина хранится
    _t = i // val and light_power[c] > _t  # тут у нас считается то, насколько можно пойти вверх
    if _t > light_power[c]:
        _t = light_power[c]
    while _t != 0:
        middle_list.append(int(i - 7 * _t))
        _t -= 1

print(f"middle list: {middle_list}")
