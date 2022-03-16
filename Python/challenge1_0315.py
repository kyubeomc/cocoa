# making a Calculater 
# Kyubeom Choi 
# 03.15.2022

def plus(number_one, number_two):
    return int(number_one) + int(number_two)

def minus(number_one, number_two):
    return int(number_one) - int(number_two)

def times(number_one, number_two):
    return int(number_one) * int(number_two)

def division(number_one, number_two):
    return int(number_one) / int(number_two)

def negation(number_one):
    return -int(number_one)

def power(number_one, number_two):
    return int(number_one) ** int(number_two)

def remind(number_one, number_two):
    return int(number_one) % int(number_two)


print(plus("10","9"))
print(minus("10","8"))
print(times(9,3))
print(division("10","4"))
print(negation("90"))
print(power(10,"4"))
print(remind(10,"4"))