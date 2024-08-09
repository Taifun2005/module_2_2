first = int(input('Введите значение first:'))
second = int(input('Введите значение second:'))
third = int(input('Введите значение third:'))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
