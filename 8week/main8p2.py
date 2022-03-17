import pandas as pd


def first_part():
    pd_series = pd.read_excel('SaleData.xlsx')
    return pd_series.head()


def second_part(colums):
    pd_series = pd.read_excel('SaleData.xlsx', usecols=[colums])
    return pd_series


def part_3():
    pd_series = pd.read_excel('SaleData.xlsx')
    table = pd.pivot_table(pd_series, index=["Region", "Manager", "SalesMan"], values="Sale_amt")
    return table.query('Manager == ["Douglas"]')


c = 0
if __name__ == '__main__':
    while True:
        answer = input('Введите, какой номер вы хотите проверить на Pandas или напишите "out":  ')
        if answer == 'out':
            print('Спасибо за внимание!')
            break
        elif answer == '1':
            print(first_part())
        elif answer == '2':
            a = input('Какие колонки вас интересуют?')
            try:
                print(second_part(a))
            except ValueError as p:
                print(f'Вы получили такую ошибку: {p}')

        elif answer == '3':  # Нашел решение в интернете, но загуглил каждый аргумент
            print(part_3())
        else:
            c += 1
            print('Не корректное значение, всего 3 номера')
            if c == 3:
                break
