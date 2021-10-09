
def doublePay(days):
    pay = 0
    base = 1
    for i in range(days):
        pay = pay + base
        base = base * 2
    return pay

print(doublePay(3))