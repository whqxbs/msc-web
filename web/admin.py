from django.contrib import admin
from .models import *

class AnswersInline(admin.TabularInline):
    model = Answers

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','sex', 'email', 'c_time')
    list_filter = ('sex', 'status')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('-c_time',)
    list_editable = ('status',)
    inlines = [AnswersInline]

    readonly_fields = ('name', 'sex', 'email', 'birth', 'qq', 'phone', 'self_introduction')
    fieldsets = (
        ('基本信息', {
            "fields": (
                'name', 'sex', 'email', 'birth', 'qq', 'phone', 'self_introduction'
            ),
        }),
        ('面试状态', {
            "fields": (
                'status',
            ),
        }), 
    )

admin.site.register(User, UserAdmin)

admin.site.register([Questions])





