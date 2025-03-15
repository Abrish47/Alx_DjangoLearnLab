from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets.ModelViewSet
from rest_framework import permissions.IsAuthenticated

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Add this

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
