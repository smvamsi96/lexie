from django.shortcuts import render
from django.http import HttpResponse
from grey.models import FileClass, FileItem

# All variables and custom functions here

file_classes = FileClass.objects.all()
con = {'app_name': 'Lexie', 'creator': 'smvamsi96', 'file_classes': file_classes,}

# Create your views here.

def grey_index(request):
   return render(request, 'grey/home.html', context=con)

def show_file_class(request, file_class_id):
    try: 
        class_of_file = FileClass.objects.get(id=file_class_id)
        files = FileItem.objects.filter(file_class=class_of_file)
        context = {'class_of_file': class_of_file, 'files': files, 'grey': '/grey/'}
    except FileClass.DoesNotExist:
        context = {'class_of_file': None, 'files': None,}

    return render(request, 'grey/items.html', context=context)
