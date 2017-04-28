# coding: utf-8
from django.core.management.base import BaseCommand

from oauth2_provider.models import Application, generate_client_id
from guestbook.models import CustomUser as User
from guestbook.client_api import GuestbookAPI


class Command(BaseCommand):
    """
    Example
    """
    help = "Example"

    def add_arguments(self, parser):
        parser.add_argument("--domain", required=False)
        parser.add_argument("--username", required=True)
        parser.add_argument("--password", required=True)

    def handle(self, *args, **options):
        api = GuestbookAPI(
            domain=options["domain"],
            username=options["username"],
            password=options["password"],
        )

        print("Регистрируем нового пользователя")
        r = api.registration()
        print(r)
        print("-" * 30)

        user = User.objects.get(username=r["json"]["username"])

        print("Пробуем повторно зарегистрироваться с теми же данными")
        r = api.registration()
        print(r)
        print("-" * 30)

        print("Создаем новое приложение для пользователя(oauth2)")
        app = Application.objects.create(
            user=user,
            authorization_grant_type=Application.GRANT_PASSWORD,
            client_type=Application.CLIENT_CONFIDENTIAL,
            name="{username}_app".format(username=user.username)
        )
        api.client_id = app.client_id
        api.client_secret = app.client_secret
        print(app.client_id, app.client_secret)

        print("-" * 30)
        print("Авторизуемся")
        r = api.auth()
        print(r)
        print("-" * 30)

        print("Получаем список всех отзывов на первой странице")
        r = api.review_list()
        print(r)
        print("-" * 30)

        print("Получаем список всех отзывов на второй странице")
        r = api.review_list(page=2)
        print(r)
        print("-" * 30)

        print("Добавляем отзыв без пар-ра text")
        r = api.review_add(page=2, foo="bar")
        print(r)
        print("-" * 30)

        print("Добавляем отзыв")
        r = api.review_add(page=2, foo="bar", text="Added review from example")
        print(r)
        print("-" * 30)
        review_id = r["json"]["id"]

        print("Получаем список всех отзывов на первой странице")
        r = api.review_list()
        print(r)
        print("-" * 30)

        print("Получаем только что созданный отзыв")
        r = api.review_detail(pk=review_id)
        print(r)
        print("-" * 30)

        print("Обновляем данные отзыва")
        # здесь специально добавлен всякий мусор и поля модели которые не будут изменены(author, reply_set)
        r = api.review_update(pk=review_id, foo="bar", page=2, text="Hello, world!(UPDATED)", author=1, reply_set=[12])
        print(r)
        print("-" * 30)

        print("Получаем только что измененный отзыв")
        r = api.review_detail(pk=review_id)
        print(r)
        print("-" * 30)

        print("Пробуем изменить отзыв созданные не этим пользователем review_id=1")
        # здесь специально добавлен всякий мусор и поля модели которые не будут изменены(author, reply_set)
        r = api.review_update(pk=1, text="Hello, world!(UPDATED)")
        print(r)
        print("-" * 30)

        print("Добавляем ответ на отзыв")
        r = api.reply_add(review=review_id, text="Reply from example")
        print(r)
        print("-" * 30)
        reply_id = r["json"]["id"]

        print("получаем отзыв с ответом")
        r = api.review_detail(pk=review_id)
        print(r)
        print("-" * 30)

        print("просто ответом")
        r = api.reply_detail(pk=reply_id)
        print(r)
        print("-" * 30)

        print("Обновляем ответ на отзыв")
        r = api.reply_update(pk=reply_id, review=review_id, text="Reply from example(UPDATED)")
        print(r)
        print("-" * 30)

        print("пробуем обновить ответ на отзыв не этого юзера")
        r = api.reply_update(pk=1, review=1, text="Reply from example(UPDATED)")
        print(r)
        print("-" * 30)

        print("Все ответы на отзывы")
        r = api.reply_list()
        print(r)
        print("-" * 30)

        print("Удаляем отзыв")
        r = api.review_delete(pk=review_id)
        print(r)
        print("-" * 30)

        print("Пробуем получить удаленный отзыв")
        r = api.review_detail(pk=review_id)
        print(r)
        print("-" * 30)

        print("Пробуем получить ответ(его нет т.к. каскадное удаление)")
        r = api.reply_detail(pk=reply_id)
        print(r)
        print("-" * 30)

        print("Список пользователей")
        r = api.user_list()
        print(r)
        print("-" * 30)

        print("детали пользователя")
        r = api.user_detail(pk=user.pk)
        print(r)
        print("-" * 30)

        print("Обновляем данные пользователя")
        r = api.user_update(pk=user.pk, email="developer@site.loc", username=user.username, password=user.password)
        print(r)
        print("-" * 30)

        print("детали пользователя")
        r = api.user_detail(pk=user.pk)
        print(r)
        print("-" * 30)

        print("Удаляем пользователя")
        r = api.user_delete(pk=user.pk)
        print(r)
        print("-" * 30)
