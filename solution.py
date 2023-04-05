import pandas as pd
import numpy as np


chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    sum = 0
    mean = x.mean()
    for i in range(len(x)):
        sum += (x[i]-mean)**2
    return 1/(n-1)*sum # Ваш ответ
