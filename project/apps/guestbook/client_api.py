# coding: utf-8
import requests

from urlparse import urljoin

from django.urls import reverse

from .conf import settings


class GuestbookAPI(object):
    """
    Класс клиентской API для пользования серивсом
    """
    def __init__(self, username=None, password=None, client_id=None, client_secret=None, domain=None):
        self.username = username or settings.GUESTBOOK_USERNAME
        self.password = password or settings.GUESTBOOK_PASSWORD
        self.client_id = client_id or settings.GUESTBOOK_CLIENT_ID
        self.client_secret = client_secret or settings.GUESTBOOK_CLIENT_SECRET
        self.domain = domain or settings.GUESTBOOK_DOMAIN
        self.request_headers = None

    def process_response(func):
        """
        Декоратор для обработки ответа
        :param func: декорируемая функция
        :return: dict ответ
        """
        def wrapper(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            result = {
                "status_code": response.status_code,
                "url": response.url,
            }
            try:
                result["json"] = response.json()
            except ValueError:
                if response.status_code >= 500:
                    result["json"] = {"error": "Server error"}
                else:
                    result["json"] = {"data": "no data"}

            return result

        return wrapper

    @process_response
    def registration(self, username=None, password=None, **kwargs):
        """
        Функция регистрации нового пользователя
        :param username: username если не указан в conf.settings
        :param password: password если не указан в conf.settings
        :param kwargs: доп данные, например, email
        :return:
        """
        data = {
            "username": username or self.username,
            "password": password or self.password
        }
        data.update(kwargs)
        response = requests.post(
            urljoin(self.domain, reverse("guestbook:customuser-list")),
            data=data
        )
        if response.status_code == 201:
            self.username = username or self.username
            self.password = password or self.password

        return response

    @process_response
    def auth(self, username=None, password=None, client_id=None, client_secret=None):       #TODO: не забыть про scope
        """
        Аутентификация пользователя
        Получаем access_token и формируем необходимый header
        :param username: username, username если не указан в conf.settings
        :param password: password, если не указан в conf.settings
        :param client_id: client_id, если не указан в conf.settings
        :param client_secret: client_secret, если не указан в conf.settings
        :return:
        """
        response = requests.post(
            urljoin(self.domain, reverse("oauth2_provider:token")),
            data={
                "grant_type": "password",
                "username": username or self.username,
                "password": password or self.password,
            },
            auth=(
                client_id or self.client_id,
                client_secret or self.client_secret
            )
        )
        if response.status_code == 200:
            # запоминаем верные данные
            self.username = client_id or self.username
            self.password = client_id or self.password
            self.client_id = client_id or self.client_id
            self.client_secret = client_id or self.client_secret
            # формируем заголовок
            content_json = response.json()
            self.request_headers = {
                "Authorization": "{token_type} {access_token}".format(
                    token_type=content_json["token_type"],
                    access_token=content_json["access_token"]
                )
            }

        return response

    @process_response
    def review_add(self, **kwargs):
        return requests.post(
            urljoin(self.domain, reverse("guestbook:review-list")),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def review_update(self, pk, **kwargs):
        return requests.put(
            urljoin(self.domain, reverse("guestbook:review-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def review_delete(self, pk, **kwargs):
        return requests.delete(
            urljoin(self.domain, reverse("guestbook:review-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def review_detail(self, pk):
        return requests.get(
            urljoin(self.domain, reverse("guestbook:review-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
        )

    @process_response
    def review_list(self, page=1, **kwargs):
        params = {"page": page}
        params.update(kwargs)
        return requests.get(
            urljoin(self.domain, reverse("guestbook:review-list")),
            headers=self.request_headers,
            params=params
        )

    @process_response
    def reply_add(self, **kwargs):
        return requests.post(
            urljoin(self.domain, reverse("guestbook:reply-list")),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def reply_detail(self, pk):
        return requests.get(
            urljoin(self.domain, reverse("guestbook:reply-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
        )

    @process_response
    def reply_update(self, pk, **kwargs):
        return requests.put(
            urljoin(self.domain, reverse("guestbook:reply-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def reply_delete(self, pk, **kwargs):
        return requests.delete(
            urljoin(self.domain, reverse("guestbook:reply-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def reply_list(self, page=1, **kwargs):
        params = {"page": page}
        params.update(kwargs)
        return requests.get(
            urljoin(self.domain, reverse("guestbook:reply-list")),
            headers=self.request_headers,
            params=params
        )

    @process_response
    def user_update(self, pk, **kwargs):
        return requests.put(
            urljoin(self.domain, reverse("guestbook:customuser-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def user_delete(self, pk, **kwargs):
        return requests.delete(
            urljoin(self.domain, reverse("guestbook:customuser-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
            data=kwargs
        )

    @process_response
    def user_list(self, page=1, **kwargs):
        params = {"page": page}
        params.update(kwargs)
        return requests.get(
            urljoin(self.domain, reverse("guestbook:customuser-list")),
            headers=self.request_headers,
            params=params
        )

    @process_response
    def user_detail(self, pk):
        return requests.get(
            urljoin(self.domain, reverse("guestbook:customuser-detail", kwargs={"pk": pk})),
            headers=self.request_headers,
        )

    process_response = staticmethod(process_response)
