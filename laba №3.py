# ввод данных и их проверка
k, i, m, n = map(int, input("Введите данные через пробел, в одну строку -").split())
figura = input("Какая фигура расположена на поле (с большой буквы) к ,i -")
if k + i + m + n > 32:
    print("Данные неверны.")

# проверка цвет поля
if ((k + i) % 2 == 0 and (m + n) % 2 == 0) or ((k + i) % 2 != 0 and (m + n) % 2 != 0):
    print("Поля одного цвета.")
else:
    print("Поля разного цвета.")

# проверка ферзь
if figura == "Ферзь":
    for j in range(9):
        if k == m or n == k or m + n == k + 1j:
            print("Ферзь угрожает фигуре.")
            break
        else:
            print("Ферзь не угрожает фигуре.")
            break
# проверка ладьи
elif figura == "Ладья":
    if k == m or i == n:
        print("Ладья угрожает фигуре.")
    else:
        print("Ладья не угрожает фигуре.")