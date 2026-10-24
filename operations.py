op = 0
n = int(input('Введите число:'))
if n >= 1 and n <= 100000:
    while n > 0:
        if(n % 3 == 0):
            n -= 3
        elif(n % 3 == 1):
            n -= 1
        elif(n % 3 == 2):
            n -= 2
        op += 1
    print('Количество операция:', op)