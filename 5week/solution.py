import numpy as np
import pandas as pd


result_dict = {}  # тут словарь всех произведений

path1 = input('Введите путь до 1 файла: ')  # файл со статьями papers001.csv
path2 = input('Введите путь до 2 файла: ')  # файл с отзывами links001.csv


data1 = pd.read_csv('papers001.csv', delimiter=';')
print(data1)


data2 = pd.read_csv('links001.csv', delimiter=';')
print(data2)

g = (data1[data1['id'] == '2'].sort_values(by='id', ascending=False).head(3))
print(g)

for i in data1['title']:
    result_dict[i] = []

print(result_dict)
