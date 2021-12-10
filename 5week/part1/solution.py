import numpy as np
import pandas as pd


# def parser_csv(data1, data2):
#     result_dict = {}  # тут словарь всех произведений
#     for i in data1[data1['title']]:  # isin сохраняет только уникальные значения, аналога пока что не нашел
#         if i in (data2['reference']):
#             if i in result_dict:
#                 result_dict[i] += 1
#             else:
#                 result_dict[i] = 1
#     print(result_dict)
#
#
# def main():
#     try:
#         data1 = pd.read_csv('papers001.csv', delimiter=';')
#         data2 = pd.read_csv('links001.csv', delimiter=';')
#     except FileNotFoundError as Er:
#         return f"Вы не правильно указали файл: {Er}"
#     else:
#         try:
#             return parser_csv(data1, data2)
#         except:
#             pass

result_dict = {}  # тут словарь всех произведений
data1 = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\HomeTask_ZFTSH\5week\part1\papers001.csv', delimiter=';')
data2 = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\HomeTask_ZFTSH\5week\part1\links001.csv', delimiter=';')

DataFrame1 = pd.DataFrame()
col, cor = np.where(data1.values == 5)

print(data1['title'] == data2['reference'])


# for i in data1[data1['title']]:  # isin сохраняет только уникальные значения, аналога пока что не нашел
#     if i in (data2['reference']):
#         if i in result_dict:
#             result_dict[i] += 1
#         else:
#             result_dict[i] = 1


# if __name__ == '__main__':
#     path1 = input('Введите путь до 1 файла: ')  # файл со статьями papers001.csv
#     path2 = input('Введите путь до 2 файла: ')  # файл с отзывами links001.csv
#     main()
