from pyDatalog import pyDatalog

pyDatalog.create_terms('result, X')
result[X] = (1 + X) / 2
print(result[100]==X)
