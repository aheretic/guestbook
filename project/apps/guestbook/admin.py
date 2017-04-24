# coding: utf-8
from django.contrib import admin

from .models import CustomUser, Review, Reply


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("get_username", )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", )


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ("id", )
