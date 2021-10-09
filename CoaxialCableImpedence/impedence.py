import math

def impedence(Dd, Dc, er):
    impedence = (138*math.log(Dd/Dc, 10))/(math.sqrt(er))
    impedence = round(impedence, 1)
    return impedence

print(impedence(4.58, 1.33, 2.2))