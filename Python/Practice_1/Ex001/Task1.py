#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#- 6 -> да
#- 7 -> да
#- 1 -> нет

check = "1234567"
numb = input('Введите число от 1 до 7: ')
while len(numb) != 1 or (numb not in check):
    print('Нужно число от 1 до 7!')
    numb = input('Введите число от 1 до 7: ')
numb = int(numb)
if numb == 6 or numb == 7:
    print(f'Да {numb} - это выходной день.')
else:
    print(f'Нет {numb} - это будний день.')
    