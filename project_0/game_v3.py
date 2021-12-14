'''Игра угадай число. Задача компьютера не более чем за 20 попыток отгадать число от 1 до 100'''

import numpy  as np
from numpy import random

def game_v3(number:int = 1) -> int:
    """ Ищем число путем деления заданной области пополам
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0   # счетчик попыток
    prdict_number_min = 1  # нижняя граница поиска числа
    prdict_number_max = 101  # верхняя граница поиска числа
    
    
    while True:
        count+=1
        
        predict_number = (prdict_number_min + prdict_number_max) // 2

        if number > predict_number:
            prdict_number_min = predict_number  # смещение нижней границы поиска числа

        elif number < predict_number:
            prdict_number_max = predict_number  # смещение верхней границы поиска числа

        else:
            break   # выход из цыкла   
        
    return count


def score_game(game_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_v3(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    #RUN
    score_game(game_v3)