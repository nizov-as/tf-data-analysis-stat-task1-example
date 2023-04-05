import pandas as pd
import numpy as np


chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    sum = 0
    mean = x.mean()
    n = len(x)
    for i in range(n):
        sum += (x[i]-mean)**2
    return (1/n)*sum # Ваш ответ
