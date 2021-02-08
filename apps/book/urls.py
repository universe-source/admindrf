# coding:utf8
from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('admin/book', views.BookViewSet)
router.register('admin/booklabel', views.BookLabelViewSet)

# 使用自动URL路由连接我们的API。
urlpatterns = [
    url(r'', include(router.urls)),
]
