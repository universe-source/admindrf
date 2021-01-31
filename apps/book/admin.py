"""
利用 ModelAdmin 来注册可以在管理界面编辑的模型
"""
from django.contrib import admin

from .models import Book, BookLabel


@admin.register(Book)  # 方法 3: 使用装饰器
class BookAdmin(admin.ModelAdmin):
    """ 书籍管理类 """
    pass


# admin.site.register(Book, BookAdmin)  # 方法 1: 自定义 Admin
admin.site.register(BookLabel)  # 方法 2: 选择默认的实现
