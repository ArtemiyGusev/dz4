# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__


# Сделали функцию, которая печает читаемое имя переданной функции и значений аргументов
def write(call_func, *args):
    print(call_func.__name__.replace('_', ' ').capitalize())
    print(*args)
    print('---')


# Вызвали функции внутри каждой функции
def open_browser(browser_name):
    write(open_browser, browser_name)
    pass


def go_to_companyname_homepage(page_url):
    write(go_to_companyname_homepage, page_url)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    write(find_registration_button_on_login_page, page_url, button_text)
    pass


# Вызываем все 3 функции с переданными аргументами
open_browser('1')
go_to_companyname_homepage('2')
find_registration_button_on_login_page('3', '4')
