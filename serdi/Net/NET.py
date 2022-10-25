import requests
import html2text
# Делаем GET-запрос
s = requests.get('http://xakep.ru', verify=False)
# Код ответа сервера
print(s.status_code)
# Создается экземпляр парсера
d = html2text.HTML2Text()
# Параметр, влияющий на то, как парсятся ссылки
d.ignore_links = True
# Текст без HTML-тегов
c=d.handle(s.text)
print(c)
