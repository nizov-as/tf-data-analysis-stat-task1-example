import pandas as pd
import numpy as np


chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Идея: вместо выборочной дисперсии использовать несмещённую (исправленную) дисперсию
    sum = 0
    mean = x.mean()
    n = len(x)
    for i in range(n):
        sum += (x[i]-mean)**2
    return 1/(n-1)*sum # Ваш ответ
