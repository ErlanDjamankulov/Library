from rest_framework import viewsets
from .models import *
from .serializers import *


class PublisherViewSets(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class LanguageViewSets(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookPhotoViewSets(viewsets.ModelViewSet):
    queryset = BookPhoto.objects.all()
    serializer_class = BookPhotoSerializer


class AuthorPhotoViewSets(viewsets.ModelViewSet):
    queryset = AuthorPhoto.objects.all()
    serializer_class = AuthorPhotoSerializer