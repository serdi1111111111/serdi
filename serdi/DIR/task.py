import re
num = int(input('Введите первое число: '))
def isoneortwo(num):
    if(num==1):
        return 'Один'
    if(num==2):
        return 'Два'
    if isoneortwo(3) is None:
        return 'Не 1 и не 2!'
print (isoneortwo())
