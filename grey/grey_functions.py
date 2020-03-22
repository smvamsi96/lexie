import os
import re
from datetime import datetime
import math
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lexie.settings')
import django
django.setup()
from grey.models import FileClass, FileItem

the_static_path = '/Users/smvamsi/static/grey/'
GB = 1073741824
MB = 1048576
KB = 1024

# regexPatterns

VideoPattern  = re.compile(r'^.*((.mp4)|(.mkv)|(.avi)|(.mov)|(.webm))$')
ImagePattern = re.compile(r'^.*((.png)|(.jpe?g)|(.heic))$')
BookPattern = re.compile(r'^.*((.pdf)|(.epub)|(mobi))$')
DocumentPattern = re.compile(r'^.*((.txt)|(.docx)|(.html)|(.yml)|(.json)|(.py)|(.c)|(.cpp)|(.swift))$')
AppPattern = re.compile(r'^.*((.dmg)|(.apk)|(.exe)|(.iso))$')
AudioPattern = re.compile(r'^.*((.mp3)|(.wav))$')
CompressedPattern = re.compile(r'^.*((.zip)|(.gzip))$')




def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier




def check_and_add(a_file):
    if (BookPattern.search(a_file)):
        a_class = fetch_file_class('Books')
        add_file_item(a_file, a_class)
    elif (ImagePattern.search(a_file)):
        a_class = fetch_file_class('Images')
        add_file_item(a_file, a_class)
    elif (VideoPattern.search(a_file)):
        a_class = fetch_file_class('Videos')
        add_file_item(a_file, a_class)
    elif (DocumentPattern.search(a_file)):
        a_class = fetch_file_class('Documents')
        add_file_item(a_file, a_class)
    elif (AppPattern.search(a_file)):
        a_class = fetch_file_class('Apps')
        add_file_item(a_file, a_class)
    elif (AudioPattern.search(a_file)):
        a_class = fetch_file_class('AudioFiles')
        add_file_item(a_file, a_class)
    elif (CompressedPattern.search(a_file)):
        a_class = fetch_file_class('CompressedFiles')
        add_file_item(a_file, a_class)
    else :
        a_class = fetch_file_class('UnrecognizedFiles')
        add_file_item(a_file, a_class)




def fetch_file_class(name):
    i, j = FileClass.objects.get_or_create(class_name=name)
    return i




def add_file_item(name, class_of_file):
    time_now = datetime.now()
    date = f"{time_now.day}/{time_now.month}/{time_now.year}"
    time = f"{time_now.hour}:{time_now.minute}"
    f, g = FileItem.objects.get_or_create(file_name=name, file_class=class_of_file)
    if g:
        meta_data = os.stat(the_static_path + name)
        size_of_file = meta_data.st_size 
        if size_of_file > GB:
            size_of_file = size_of_file/GB
            f.file_size = f"{math.trunc(size_of_file)} GB"
        elif size_of_file > MB:
            size_of_file = size_of_file/MB
            f.file_size = f"{math.trunc(size_of_file)} MB"
        else:
            size_of_file = size_of_file/KB
            f.file_size = f"{math.trunc(size_of_file)} KB"
        f.file_date = date
        f.file_time = time
    f.save()




def update_database():
    items = os.listdir(the_static_path)
    for item in items:
        check_and_add(item)




def save_uploaded_file(uploaded_file, uploaded_file_name):
    """ Writes uploaded_file to disk """
    # the_static_path is where uploaded_file is saved
#   default_path = '/Users/smvamsi/static/grey/'
    new_file = the_static_path + uploaded_file_name
    with open(new_file, 'wb+') as new_file:
        for chunk in uploaded_file.chunks():
            new_file.write(chunk)
