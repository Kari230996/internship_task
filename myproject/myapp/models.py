from django.db import models

# Create your models here.


# Пользователь
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
# Продукт
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
# Доступ к продукту для пользователя
class Access(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Доступ к продукту {self.product.product_name} имеет пользователь {self.user.username}"
    
# Урок
class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)
    duration_seconds = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson_name

# Просмотр урока
class LessonView(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_time_seconds = models.IntegerField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} посетил {self.lesson.lesson_name}"


    


