# coding: utf-8
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Право позволяющее выполнять действия только над теми объектами автором которых является текущий юзер
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsThisUserOrReadOnly(permissions.BasePermission):
    """
    Право позволяет выполнять юзеру действия только над собственными данными
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Права на чтение или изменения только для суперюзера
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser
