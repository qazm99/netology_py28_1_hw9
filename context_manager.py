#алгоритм вычисления Пи был взят на просторах интернета
import datetime, decimal
from math import factorial


class Date_logger:
    def __init__(self):
        self.date_start = datetime.datetime.now()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.date_stop = datetime.datetime.now()
        print(f"Время старта {self.date_start}")
        print(f"Время окочания {self.date_stop}")
        print(f"Затрачено для вычислений {(self.date_stop - self.date_start).seconds: .0F} секунд")

# Фильтр только целые положительные числа
def posintput(string):
    while True:
        integer = input(string)
        if integer.isdigit():
            return int(integer)
        else:
            print("Нужно ввести целое положительное число")

# Вычисление Пи
def chudnovsky(n):
    pi = decimal.Decimal(0)
    k = 0
    while k < n:
        pi += (decimal.Decimal(-1) ** k) * (decimal.Decimal(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (
                    13591409 + 545140134 * k) / (640320 ** (3 * k)))
        k += 1
        print("Шаг: {} из {}".format(k, n))
    pi = pi * decimal.Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)
    return pi


if __name__ == '__main__':
    while True:
        number_sign = posintput("Сейчас попробуем вычислись число Пи. Введите число знаков после запятой: ")
        with Date_logger():
            #print("Начало программы")
            decimal.getcontext().prec = number_sign
            pi_result = chudnovsky(number_sign / 14)
            print(f"Число Пи: {pi_result}")
        if input("Попробуем еще?(Да/Нет): ").upper() != 'ДА':
            break






