from calc import Calc

if __name__ == '__main__':
    calc = Calc()
    try:
        print(calc.divide(3, 0))
    except ZeroDivisionError:
        print('hello kek')
    print(calc.sum(0.0000001, 0.00000007))
    print(calc.sum(700987100000.0, 15700987100666.0))
    for i in range(22):
        print(i, calc.factorial(i))
    print(calc.subtract(5, 3))
