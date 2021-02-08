# coding:utf8
"""
书籍库: 存储所有读过或者被网站文章引用的书籍信息
"""
from django.db import models

from utils.const_variable import ConstInt


class BookLabel(models.Model):
    """ 书籍分类, 比如社科, 技术-python这样分类 """
    name = models.CharField(
        verbose_name='书籍分类', max_length=ConstInt.LEN_32, db_index=True)
    alias = models.CharField(verbose_name='分类别名', max_length=ConstInt.LEN_32)
    description = models.CharField(
        verbose_name='别名介绍', max_length=ConstInt.LEN_128)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'booklabel'
        verbose_name = '书籍分类:社科,技术等'


class Book(models.Model):
    """ 书籍表
        1. 嵌套对象: 书籍信息((标签信息), 其他信息)
    """
    bookid = models.AutoField(primary_key=True)  # 自增 ID
    name = models.CharField('书籍名称', max_length=ConstInt.LEN_64, db_index=True)
    publish = models.CharField(verbose_name='出版社', max_length=ConstInt.LEN_64)
    author = models.CharField(verbose_name='作者', max_length=ConstInt.LEN_32)
    booklabel = models.ForeignKey(
        BookLabel, verbose_name='书籍分类外键ID', on_delete=models.PROTECT)
    description = models.TextField(verbose_name='书籍描述信息')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'  # 表名
        verbose_name = '一个描述出版书籍的表信息'  # 描述
        indexes = [  # 索引
            models.Index(fields=['name', 'author'])
        ]
