from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets.ModelViewSet

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
