from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from grey.models import FileClass, FileItem
from grey.forms import UploadFileForm
# import custom functions from a pythonpath(find out yours from sys.path  and place a symlink of your module in that path)
import grey_functions as g




# All variables and custom functions here




global_context_dictionary = {'app_name': 'Lexie', 'creator': 'smvamsi96', 'all_file_classes': FileClass.objects.all(),}




# Create your views here.
# A local_context_dictionary is function specific




def upload_file(request):
    """ Handles file upload """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name_of_the_uploaded_file = request.FILES['the_file'].name
            g.save_uploaded_file(request.FILES['the_file'], name_of_the_uploaded_file)
            g.update_database()
            local_context_dictionary = {'message': f"The File {name_of_the_uploaded_file} Uploaded Successfully",} 
            local_context_dictionary.update(global_context_dictionary)
            return render(request, 'grey/success.html', context=local_context_dictionary)
    else:
        form = UploadFileForm()
    local_context_dictionary = {'form': form,}
    local_context_dictionary.update(global_context_dictionary)
    return render(request, 'grey/upload.html', context=local_context_dictionary)




def grey_index(request):
    """ Handles the Homepage """
    return render(request, 'grey/home.html', context=global_context_dictionary)




def show_file_class(request, file_class_id):
    """ Lists all the items in a class """
    try: 
        class_of_file = FileClass.objects.get(id=file_class_id)
        files = FileItem.objects.filter(file_class=class_of_file)
        local_context_dictionary = {'class_of_file': class_of_file, 'files': files, 'grey': '/grey/'}
        local_context_dictionary.update(global_context_dictionary)
    except FileClass.DoesNotExist:
        local_context_dictionary = {'class_of_file': None, 'files': None,}

    return render(request, 'grey/items.html', context=local_context_dictionary)
