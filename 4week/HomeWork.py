"""
Калинин Егор 9 класс
27.11.21
"""
import csv
import heapq
import matplotlib.pyplot as plt

"""
Ex 1
"""


companies = []
max_8plus = []
max_oll = []
inp1 = input('Введите путь 1: ')  # 1637855815644_rates001.csv
inp2 = input('Введите путь 2: ')  # 1637855798464_games001.csv

kay = 0
total_prices = {}
with open(inp1, encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for i in reader:
        value = i[0].split(';')
        if value[0] not in total_prices:
            total_prices[value[0]] = [int(value[1])]
            if int(value[1]) >= 8.0:
                total_prices[value[0]].append(1)
            else:
                total_prices[value[0]].append(0)
        else:
            total_prices[value[0]][0] += int(value[1])
            if int(value[1]) >= 8.0:
                total_prices[value[0]][1] += 1

print(total_prices)

with open(inp2, encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for i in reader:
        value = i[0].split(';')
        total_prices[value[0]].append(value[1])
print(total_prices)


for i in total_prices.values():
    max_oll.append(i[0])
    max_8plus.append(i[1])
    companies.append(i[2])


def max_three(li, company):
    top3 = heapq.nlargest(3, li)
    return top3, [company[0], company[1], company[2]]


a = max_three(max_oll, companies)
b = max_three(max_8plus, companies)


plt.ylabel('All Marks')
plt.xlabel('Companies')
plt.bar(a[1], a[0], color=['red', 'blue', 'green'])
plt.show()
