user_input = input("Введите b, q и n через пробел: ")

parts = user_input.split()
b = int(parts[0])
q = int(parts[1])
n = int(parts[2])

summa = b * (q**n - 1) // (q - 1)

print(summa)