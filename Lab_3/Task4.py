from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('median, result, X')
result[X] = random.randint(1, 100) + result[X - 1]
result[0] = 0
median[X] = result[X] / X
print(median[100]==X)
