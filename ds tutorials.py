from collections import Counter
import math
import numpy as np

moto = np.random.randn(40)
x = [1,2,5,3,6]
y = [1,2,1,1,3,2,4]
z = [0,100]

def mean(x):
    #v = 0
    #for i in x:
     #   v = v + i
    #return v / len(x)

     return sum(x) / len(x)

def median(x):
    sorted_x = sorted(x)
    n = len(x)
    midpoint = n // 2 

    # Modulo operator
    if n % 2 == 1:
        return sorted_x[midpoint]

    else:
        hi = midpoint
        lo = midpoint - 1
        return (sorted_x[hi] + sorted_x[lo]) / 2

# QuickSelect

def quantile(x, p):
    p_index = int(len(x) * p)

    return sorted(x)[p_index]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

# Dispersion

def rng(x):
     return max(x) - min(x)

def de_mean(x):
     x_bar = mean(x)
     return [(x_i - x_bar) ** 2 for x_i in x]

def variance(x):
     n = len(x)
     deviations = de_mean(x)
     return sum(deviations) / (n-1)

def standard_dev(x):
     return math.sqrt(variance(x))

def interquartile_range(x):
     return quantile(x, 0.75) - quantile(x, 0.25)

def de_mean_unsquare(x):
     x_bar = mean(x)
     return [(x_i - x_bar) for x_i in x]

def covariance(x, y):
     n = len(x)
     return np.dot(de_mean_unsquare(x), de_mean_unsquare(y)) / (n-1)

def correlation(x, y):
     std_x = standard_dev(x)
     std_y = standard_dev(y)
     if std_x > 0 and std_y > 0:
          return covariance(x, y) / std_x / std_y
     else:
          return 0
     
