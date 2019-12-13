# Створити клас для виконання операцій з комплексними числами.
# Передбачити операції: складання та віднімання; множення та ділення; обчислення модулю;
# консольне введення та виведення; ініціалізацію.

import math


class Complex():
    """"Complex number"""

    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        reverse = float(other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real + self.imag * other.imag) / reverse,
                       (self.imag * other.real - self.real * other.imag) / reverse)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __str__(self):
        return '({} + {}i)'.format(self.real, self.imag)

    def input(self):
        string = input('Complex number (x + yi) - ')              

        real_index = string.find('+')
        imag_index = string.find('i')

        if (real_index != -1 and imag_index != -1):
            self.real = float(string[:real_index])
            self.imag = float(string[real_index + 1:imag_index])
        else:
            self.real = float(string)

    def print(self):
        print(self)


x = Complex()
x.input()
x.print()

y = Complex()
y.input()
y.print()

print("Addition = " + str(x+y))
print("Subtraction = "+ str(x-y))
print("Multiplication = "+ str(x*y))
print("Division = "+ str(x/y))
print("Abs x = " + str(abs(x)))