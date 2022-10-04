def counter(a, b, c):
    if a == 0: 
        print("Вы ввели не квадратное уравнение")
        return []
    d = b**2 - 4 * a * c

    if d >= 0:
        return [(-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)]
    

    print("Нет решений")
    return []