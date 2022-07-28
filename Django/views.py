import random
from django.http import HttpRequest, HttpResponse


def password_gen(request, length: int) -> HttpResponse:
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ''
    for len in range(length):
        random_char = random.choice(chars)
        password += random_char
    list_pass = list(password)
    random.shuffle(list_pass)
    generated_password = ''.join(list_pass)
    print(generated_password)
    return HttpResponse(f'New password was generated: {generated_password}')


def check_password(request, password: str) -> HttpResponse:
    special_characters = '!@#$%&()-_[]{};:"./<>?'
    if any(map(lambda x: x in password, special_characters)) or len(password) != 8:
        return HttpResponse('Password have denied characters or length')
    else:
        return HttpResponse('Password is ok!')


def home(request: HttpRequest) -> HttpResponse:
    response = f"""
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="robots" content="noindex, nofollow">
        <title>Сайт на реконструкции</title>
    </head>
    <body bgcolor="#c0c0c0">
        <main>
            <H1>ГРЯДЯЕТ НОВЫЙ СТАРТ!</H1>
            <p>Наш сайт находится в стадии разработки, и мы почти готовы к работе!<br>
    Мы готовим для вас нечто удивительное и захватывающее - специальный сюрприз для подписчиков</p>
       </main>
    </body>
    </html>
    """
    return HttpResponse(response)


def article(request, article_id: int, article_slug: str) -> HttpResponse:
    response = f"""
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="robots" content="noindex, nofollow">
        <title>{article_slug}</title>
    </head>
    <body bgcolor="#c0c0c0">
        <main>
            <H1>Статья под номером {article_id}</H1>
            <H1>{article_slug}</H1>
       </main>
    </body>
    </html>
        """
    return HttpResponse(response)
