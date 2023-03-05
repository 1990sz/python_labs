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


# Перебираем все числа от 10 до 9999
for number in range(10, 10000):
    if is_armstrong(number):
        print(number)
