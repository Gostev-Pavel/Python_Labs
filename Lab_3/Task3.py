from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('result, X')
result[X] = random.randint(1, 100) * result[X - 1]
result[0] = 1
print(result[100]==X)
