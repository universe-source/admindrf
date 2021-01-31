from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'booklabels', views.BookLabelViewSet)

# 使用自动URL路由连接我们的API。
urlpatterns = [
    path('', include(router.urls)),
]
