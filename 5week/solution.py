import numpy as np
import pandas as pd


path1 = input('Введите путь до 1 файла: ')  # файл со статьями papers001.csv
path2 = input('Введите путь до 2 файла: ')  # файл с отзывами links001.csv


data1 = pd.read_csv('papers001.csv', delimiter=';')
print(data1)
