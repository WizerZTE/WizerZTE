result = []
def divider(a, b):
    if a < b:
        raise ValueError("Дільник більший за чисельник.")
    if b > 100:
        raise IndexError("Значення дільника перевищує 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        a = int(key)
        b = data[key]
        res = divider(a, b)
        result.append(res)
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль для ключа {key}.")
    except ValueError as ve:
        print(f"Помилка значення для ключа {key}: {ve}.")
    except IndexError as ie:
        print(f"Помилка індексу для ключа {key}: {ie}.")
    except TypeError as te:
        print(f"Помилка типу для ключа {key}: {te}.")
    except Exception as e:
        print(f"Невідома помилка для ключа {key}: {e}.")

print("Результат:", result)
