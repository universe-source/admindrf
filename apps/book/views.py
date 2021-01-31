from django.shortcuts import render
from rest_framework import viewsets

from .models import Book, BookLabel

from .serializers import BookSerializer, BookLabelSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-bookid')
    serializer_class = BookSerializer


class BookLabelViewSet(viewsets.ModelViewSet):
    queryset = BookLabel.objects.all().order_by('-name')
    serializer_class = BookLabelSerializer
