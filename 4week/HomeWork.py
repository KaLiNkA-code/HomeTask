"""
Калинин Егор 9 класс
27.11.21
"""
import matplotlib
import csv
# import pandas


"""
Ex 1
"""
inp1 = input('Введите путь 1')  # 1637855815644_rates001.csv
inp2 = input('Введите путь 2')  # 1637855798464_games001.csv

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
