from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from grey.models import FileClass, FileItem
from grey.forms import UploadFileForm

# All variables and custom functions here

file_classes = FileClass.objects.all()
con = {'app_name': 'Lexie', 'creator': 'smvamsi96', 'file_classes': file_classes,}

default_path = '/Users/smvamsi/Public/'

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def handle_uploaded_file(f, the_name):
    the_name = default_path + the_name
    with open(the_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name_of_the_file = request.FILES['the_file'].name
            handle_uploaded_file(request.FILES['the_file'], name_of_the_file)
            return HttpResponse(f"SUCCESS with {name_of_the_file}")
    else:
        form = UploadFileForm()
    return render(request, 'grey/upload.html', {'form': form, 'app_name': 'Lexie'})

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
