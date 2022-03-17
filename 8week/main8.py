import numpy as np
import ast


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
        a1 = np.array(ast.literal_eval(aa1))
        a2 = np.array(ast.literal_eval(aa2))
    except TypeError as P1:
        return f"Не корректное значение! (Вот ошибка: {P1})"
    except ValueError as P2:
        return f"Не корректное значение! (Вот ошибка: {P2})"
    else:
        return np.outer(a1, a2)


"""
    a = np.array(input())
    print(type(a))
    print(solution_4([[1, 5], [3, 6]], [[1, 2], [3, 2]]))
"""

"""555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"""


def solution_5(m1):

    m1 = np.array(m1)
    #  return type(m1)  |  <class 'numpy.ndarray'>
    if np.any(m1 == 0):
        return 'Есть'
    else:
        return 'Нету'  # Всегда говорит 'Нету'


c = 0
if __name__ == '__main__':
    while True:
        answer = input('Введите, какой номер вы хотите проверить на Numpy или напишите "out":  ')
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

            a1 = input('введите 1 массив: ')
            a2 = input('введите 2 массив: ')
            print(solution_4(a1, a2))

        elif answer == '5':
            try:
                a1 = input('Введите матрицу, и я скажу, есть ли там ноль:  ')
                a = np.array(a1)
            except TypeError as P:
                print(f"Не корректное значение! (Вот ошибка: {P})")
            else:
                print(solution_5(a))
        else:
            print('Ваше значение не корректное')
            c += 1
            if c == 3:
                break
