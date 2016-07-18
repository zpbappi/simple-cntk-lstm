from numpy import arange
from math import sin

def generate_train(filePath, start=1.0, end=30.0, step=0.1):
    with open(filePath, "w") as file:
        for t in arange(start, end, step):
            f = sin(t)/t
            file.write("|t {0} |f {1}\n".format(round(t,1), f))

def generate_test(filePath, start=2.3, end=25.7, step=0.37):
    with open(filePath, "w") as file:
        for t in arange(start, end, step):
            f = sin(t)/t
            file.write("|t {0} |f {1}\n".format(round(t,2), f))

