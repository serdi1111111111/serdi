import re

f = open ('byfer.txt', 'r', encoding='UTF-8')
s = f.read()
words = s.split()
for w in words:
    n = w.find('@mail.ru')
    if n != -1:
        q = open('mail.txt', 'w', encoding='UTF-8')
        q.write(str(w)+'\n')
        with open ('mail.txt', 'a', encoding='UTF-8') as e:
            e.write(str(w)+'\n')
        print ('Найден e-mail: ' + str(w) + ' в позиции ' + str(n))
for a in words:
    s = a.find('@yandex.ru')
    if s != -1:
        d = open('yandex.txt', 'w', encoding='UTF-8')
        d.write(str(a)+'\n')
        with open ('yandex.txt', 'a', encoding='UTF-8') as f:
            f.write(str(a)+'\n')
        print ('Найден e-mail: ' + str(a) + ' в позиции ' + str(s))
for z in words:
    x = z.find('@xakep.ru')
    if x != -1:
        c = open('xaker.txt', 'w', encoding='UTF-8')
        c.write(str(z)+'\n')
        with open ('xaker.txt', 'a', encoding='UTF-8') as v:
            v.write(str(z)+'\n')
        print ('Найден e-mail: ' + str(z) + ' в позиции ' + str(x))


#Прог­рамма дол­жна сор­тировать стро­ки по доменам из email,
#для каж­дого домена соз­давать файл и в каж­дый файл помещать
#спи­сок поч­товых адре­сов.
