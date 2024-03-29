from django.db import models

class Publisher(models.Model):
    name = models.CharField("Издательство",max_length=16, unique=True)

    def __str__(self):
        return self.name
class Language(models.Model):
    name = models.CharField("Язык книги",max_length=16, unique=True)

    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField("Жанр книги",max_length=16)


    def __str__(self):
        return self.name
class Book(models.Model):
    author = models.ManyToManyField(to='Author')
    title = models.CharField(max_length=32)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    lang=models.ForeignKey(Language,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField("Имя автора",max_length=32)
    last_name=models.CharField("Фамилия автора",max_length=32)
    date_birth=models.DateField("Дата рождения",null=True)
    about=models.TextField("Об авторе")

    def __str__(self):
        return f'{self.name} - {self.last_name}'

class BookPhoto(models.Model):
    product_photo = models.ForeignKey(Book, related_name='book', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

class AuthorPhoto(models.Model):
    product_photo = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')








