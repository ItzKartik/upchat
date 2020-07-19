# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

class chatsadmin(admin.TabularInline):
    model = models.chats

class filesadmin(admin.TabularInline):
    model = models.files

@admin.register(models.group)
class group_admin(admin.ModelAdmin):
    inlines = [
        chatsadmin,
        filesadmin
    ]
