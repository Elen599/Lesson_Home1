# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def Main():
    number = int(input('Введите число: '))
    num =  number ** 16 - 1
    print(f'Число {number} в 16-ой СС = ', hex(num))

Main()