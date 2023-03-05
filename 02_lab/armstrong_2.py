# Функция для проверки, является ли число числом Армстронга
def is_armstrong(number):
    # Преобразуем число в строку, чтобы посчитать количество цифр
    num_str = str(number)
    # Получаем количество цифр в числе
    n = len(num_str)
    # Считаем сумму k-х степеней цифр числа
    sum = 0
    for digit in num_str:
        sum += int(digit) ** n
    # Проверяем, равна ли сумма числу
    return sum == number

# Генерируем список всех чисел от 10 до 9999
numbers = [x for x in range(10, 10000)]

# Фильтруем список, оставляя только числа Армстронга
armstrong_numbers = list(filter(is_armstrong, numbers))

# Выводим список чисел Армстронга на экран
print(armstrong_numbers)
