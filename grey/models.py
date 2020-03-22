# Purpose of this file:
# This file defines all your database tables and their relationships.
from django.db import models

# Create your models here.

class FileClass(models.Model):
    """ This Class classifies files into their filetypes. """
# A CharField always requires max_length attribute.
    class_name = models.CharField(max_length=25, blank=False, unique=True)
# This Meta Class defines the plural for the model.
    class Meta: 
        verbose_name_plural = 'FileClasses'
# A __str__ method defines how an object is printed.
    def __str__(self):
        return f"{ self.class_name }"


class FileItem(models.Model):
# A CharField always requires max_length attribute.
    file_name = models.CharField(max_length=60, blank=False, unique=True)
# A ForeignKey defines OneToMany Relationship between tables.
    file_class = models.ForeignKey(FileClass, on_delete=models.CASCADE)
    file_date = models.CharField(max_length=12, blank=True, unique=False)
    file_time = models.CharField(max_length=6, blank=True, unique=False)
    file_size = models.CharField(max_length=10, blank=True)
# This Meta Class defines the plural for the model.
    class Meta: 
        verbose_name_plural = 'FileItems'
# A __str__ method defines how an object is printed.
    def __str__(self):
        return f"{ self.file_name } in { self.file_class }"


