import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 411069874 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    scale = (x**2).sum() / 24
    return np.sqrt(scale / chi2.ppf(1 - alpha / 2, 2 * len(x))),
           np.sqrt(scale / chi2.ppf(alpha / 2, 2 * len(x)))
