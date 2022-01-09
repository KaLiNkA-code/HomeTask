import numpy as np


"""111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"""


def first_solution():
    return np.arange(2, 11).reshape(3, 3)


"""222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"""


def two_solution():
    matrix = np.ones((3, 3))
    return np.pad(matrix, pad_width=1)


"""333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"""


def three_solution():
    array1 = [0, 10, 20, 40, 60, 80]
    array2 = [10, 30, 40, 50, 70]
    return np.union1d(array1, array2)


"""444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444"""


def solution_4(aa1, aa2):
    try:
        np.array(aa1)
        np.array(aa2)
    except TypeError as PP:
        return f"Не корректное значение! (Вот ошибка: {PP})"
    else:
        return np.outer(aa1, aa2)


"""
    a = np.array(input())
    print(type(a))
    print(solution_4([[1, 5], [3, 6]], [[1, 2], [3, 2]]))
"""

"""555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"""


def solution_5(m1):
    # Я не знаю, как принять матрицу так, чтобы она была типом list/int чтобы это не награмождало код (try с циклом)
    #  matrix = np.array([[0, 2, 4], [-1, 4, 2], [3, 4, 2]])
    if np.any(m1 == 0):
        return 'Есть'
    else:
        return 'Нету'


c = 0
if __name__ == '__main__':
    while True:
        answer = input('Введите, какой номер вы хотите проверить или напишите "out":  ')
        if answer == 'out':
            print('Спасибо за внимание!')
            break
        elif answer == '1':
            print(first_solution())
        elif answer == '2':
            print(two_solution())
        elif answer == '3':
            print(three_solution())
        elif answer == '4':

            a12 = input('введите 1 массив: ')
            a1 = np.array([[1, 4], [2, 5]])
            a22 = input('введите 2 массив: ')
            a2 = np.array([[1, 3], [5, 7]])
            print(solution_4(a12, a22))
        elif answer == '5':
            try:
                a1 = input('Введите матрицу, и я скажу, есть ли там ноль:  ')
                a = np.array([[1, 2, 3], [3, 4, 5], [3, 2, 5]])
            except TypeError as P:
                print(f"Не корректное значение! (Вот ошибка: {P})")
            else:
                print(solution_5(a))
        else:
            print('Ваше значение не корректное')
            c += 1
            if c == 3:
                break
