import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 1126746074 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    alpha = 1 - p
    loc = x.mean()
    
    scale = np.var(x)
    return np.sqrt(scale/47) - np.sqrt((scale * len(x) / chi2.ppf(1 - alpha / 2, len(x)) ) / 47), \
           np.sqrt(scale/47) + np.sqrt((scale * len(x) / chi2.ppf(alpha / 2, len(x)) )/ 47)
