import csv
import matplotlib.pyplot as plt
import pandas as pd
# string = input()
# index = 0
# new_string = []
#
# for j in string:
#     for i in j:
#         if i in '!?.,-':
#             new_string.append(i)
#             new_string.append(' ')
#         elif i == ' ' and not new_string[-1] == ' ':
#             new_string.append(i)
#         elif index > 2:
#             if new_string[-1] == ' ' and new_string[-2] in '!?.':
#                 new_string.append(i.upper())
#             elif i != ' ':
#                 new_string.append(i)
#     index += 1
#
# print(''.join(new_string))


# for j in string:
#     for i in j:
#         if i in '!?.,-':
#             new_string += i
#             new_string += ' '
#         elif i == ' ' and not new_string[-1] == ' ':
#             new_string += i
#         elif i != ' ':
#             new_string += i
#     index += 1
#
# print(new_string)

"""номер 3 не знаю, что нужно от меня делать"""

"""Доп задания"""

"""Номер 1"""
# with open('transactions.csv', encoding='UTF-8') as file:
#     reader = csv.reader(file, delimiter=',')
#     next(reader)
#     m1 = m2 = m3 = 0
#     for i in reader:
#         if i[2] and i[2] == 'OK':
#             if int(i[3]) > m1:
#                 m3 = m2
#                 m2 = m1
#                 m1 = int(i[3])
#     print(f"{m1}, {m2}, {m3}")

"""Номер 2"""

# with open('transactions.csv', encoding='UTF-8') as file:
#     reader = csv.reader(file, delimiter=',')
#     next(reader)
#     result = 0
#     for i in reader:
#         if i[2] and i[2] == 'OK':
#             result += int(i[3])
#     print(result)


"""Номер 3"""


# with open('flights.csv', encoding='UTF-8') as file:
#     reader = csv.reader(file, delimiter=',')
#     next(reader)
#     name = []
#     dicct = {}
#     for i in reader:
#
#         if i[1] not in dicct:
#             dicct.update({i[1]: [0, 0, 0, [], [], []]})
#         else:
#             dicct[i[1]][0] += 1
#             dicct[i[1]][3].append(dicct[i[1]][0] + 1)
#             dicct[i[1]][1] += int(i[2])
#             dicct[i[1]][4].append(int(i[2]))
#             dicct[i[1]][2] += int(i[3])
#             dicct[i[1]][5].append(int(i[3]))
#     # Полная стоимость
#
#     for k, v in dicct.items():
#         print(f"Комапания {k} сделала {v[0]} перелетов, стоимость: {v[1]}, а общий вес: {v[2]}.")
#         fig, ax = plt.subplots()
#         ax.plot(linewidth=3)
#         ax.set_title(f"График {k}", fontsize=24)
#         ax.set_ylabel('Value', fontsize=14)
#         ax.set_xlabel('Number', fontsize=14)
#         ax.tick_params(axis='both', labelsize=14)
#         ax.plot(v[4], c='red')
#         plt.plot(v[5], c='green')
#         plt.plot(v[3], c='blue')
#         plt.show()


"""Номер 4"""

df = pd.read_excel('students_info.xlsx')  # Здесь данные групп от деканата
print(df)

with open('results_ejudge.html', encoding='UTF-8') as file:
    f = file.read()
    find_aLL = f.find('thead')
    print(find_aLL)
