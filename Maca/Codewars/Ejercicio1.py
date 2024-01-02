"""Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
Note: The function accepts an integer and returns an integer.
Happy Coding!"""


def square_digits1(num):
    if len(str(num)) > 1:
        resultado = (int(num / 10 ** (len(str(num)) - 1)))
        conjunto = (resultado ** 2)

        resto = (int(num % (10 ** (len(str(num)) - 1))))
        resultado2 = (int(resto / (10 ** (len(str(resto)) - 1))))
        conjunto2 = resultado2 ** 2

        resto2 = int(resto % (10 ** (len(str(resto)) - 1)))
        conjunto3 = resto2**2

        print('{}{}{}'.format(conjunto, conjunto2, conjunto3))
        return int(str(conjunto) + str(conjunto2) + str(conjunto3))
    else:
        print(num ** 2)
        return (num ** 2)



def square_digits2(num):
    conjunto = ""
    resultado = (int(num / 10 ** (len(str(num)) - 1)))  # 1
    resto = (int(num % (10 ** (len(str(num)) - 1))))  # 23
    conjunto += str(resultado ** 2)
    i = 0

    while i < len(str(num)) - 1:
        resultado = (int(resto / 10 ** (len(str(resto)) - 1)))
        resto = (int(resto % (10 ** (len(str(resto)) - 1))))
        conjunto += str(resultado ** 2)
        i += 1

    if (resto != 0):
        conjunto += (str(resto ** 2))
    print(conjunto)
    return int(conjunto)


def square_digits3(num):
    conjunto = ""
    resultado = (int(num / 10 ** (len(str(num)) - 1)))  # 1
    resto = (int(num % (10 ** (len(str(num)) - 1))))  # 23
    conjunto += str(resultado ** 2)

    for i in range(0, len(str(num)) - 1, 1):
        resultado = int(resto / 10 ** (len(str(resto)) - 1))
        resto = int(resto % (10 ** (len(str(resto)) - 1)))
        conjunto += str(resultado ** 2)
    return int(conjunto)