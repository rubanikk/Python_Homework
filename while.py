a = int(input('введите значение а: '))
b = int(input('введите значение b: '))
c = int(input('введите значение c: '))
d = str(a)

while (a < b):
    print('sad message')
    a = a + c
    d = d + ' ' + str(a)

print('happy message')
print('история инкрементов: ', d)