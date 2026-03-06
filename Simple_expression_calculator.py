# Я решила сделать задачу чуть-чуть эффективнее: мы принимаем на вход не строку.
# Строка - слишком непредсказуемый формат. Сложно парсить и находить ошибки.
# Мы ожидаем получить от пользователя определённый паттерн [число] [оператор] [число]...
# Проще запросить выражение по частям и сразу присекать ошибки.


def input_expression():
    """Запрашивает у пользователя выражение по частям: число, оператор, число..."""
    numbers = []
    operators = []
    
    while True:
        number = None
        while number is None:
            part = input("Число: ").strip()
            
            if part == '?':
                if len(numbers) == 0:
                    print("\nВы не ввели выражение!\n")
                else:
                    print("\nВыражение не может заканчиваться оператором!\n")
                continue
            
            try:
                number = float(part)
            except ValueError:
                continue
            
            if len(operators) > 0 and operators[-1] == '/' and number == 0:
                print("Нельзя делить на ноль!")
                number = None
                continue
        
        numbers.append(number)
        

        operator = None
        while operator is None:
            part = input("Оператор или '?': ").strip()
            
            if part == '?':
                if len(operators) == 0:
                    print("\nТут нечего вычислять...введите оставшуюся часть выражения.\n")
                    continue
                else:
                    return numbers, operators
            
            if part in ['+', '-', '*', '/']:
                operator = part
            else:
                continue
        
        operators.append(operator)


def calculate(numbers, operators):
    """Вычисляет результат выражения с учётом приоритета операций."""

    i = 0
    while i < len(operators):
        if operators[i] == '*':
            numbers[i] = numbers[i] * numbers[i + 1]
            numbers.pop(i + 1)
            operators.pop(i)
        elif operators[i] == '/':
            numbers[i] = numbers[i] / numbers[i + 1]
            numbers.pop(i + 1)
            operators.pop(i)
        else:
            i += 1
    

    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '-':
            result -= numbers[i + 1]
    
    return result

print("\n==Добро пожаловать==")
print("=========В=========")
print("=== Калькулятор ===")
print("\nВводите выражение по частям.\nДоступные операции: +, -, *, /.\nДля завершения ввода выражения введите '?'.\n")

numbers, operators = input_expression()
result = calculate(numbers, operators)

if result == int(result):
    result = int(result)

print(f"\nРезультат: {result}")