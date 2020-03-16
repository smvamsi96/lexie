from django.db import models

# Create your models here.

class FileClass(models.Model):
    class_name = models.CharField(max_length=25, blank=False, unique=True)

    class Meta: 
        verbose_name_plural = 'FileClasses'

    def __str__(self):
        return f"Name: { self.class_name }"


class FileItem(models.Model):
    file_name = models.CharField(max_length=60, blank=False, unique=True)
    file_class = models.ForeignKey(FileClass, on_delete=models.CASCADE)
    file_date = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name_plural = 'FileItems'

    def __str__(self):
        return f"Name: { self.file_name } in Class { self.file_class }"
