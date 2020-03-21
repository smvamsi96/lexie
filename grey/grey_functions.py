import os
import filetype
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lexie.settings')
import django
django.setup()
from grey.models import FileClass, FileItem

the_static_path='/Users/smvamsi/static/grey/'

def det_file_type(a_file):
    print('executing det_file_type')
    kind = filetype.guess(a_file)
    if kind is None:
        return
    k = kind.extension
    if k == 'pdf':
        print(k)
        return 1
    elif k == 'png' or k == 'jpeg' or k == 'jpg' or k == 'heic' or k == 'gif':
        print(k)
        return 2
    elif k == 'mp4' or k == 'mkv' or k == 'webm':
        print(k)
        return 3
    elif k == 'epub':
        print(k)
        return 4
    elif k == 'mp3':
        print(k)
        return 5
    elif k == 'txt' or k == 'html' or k == 'c' or k == 'py' or k == 'cpp':
        print(k)
        return 6

    
def symlink_the_upload_directory():
    """ Creates symlinks of files from the static directory """
    print("executing symlink_the_upload_directory")
#   origin_path = '/Users/smvamsi/static/grey/'
    destnation_path = '/Users/smvamsi/Code/lexie/grey/static/grey/'
    for uploaded_file in os.listdir(the_static_path):
        src = the_static_path + uploaded_file
        dst = destnation_path + uploaded_file
        try:
            os.symlink(src, dst)
            print(f"symlinked - {dst} - {det_file_type(dst)}")
        except FileExistsError:
            print("The File Already Exists")

def index_static_files():
    """ indexes and adds symlinks of uploaded files """
    print("executing index_static_files")
    django_symlink_path = '/Users/smvamsi/Code/lexie/grey/static/grey/'
    pdf_items = []
    image_items = []
    video_items = []
    epub_items = []
    mp3_items = []
    txt_items = []
    symlink_the_upload_directory()
    items = os.listdir(django_symlink_path)
    for item in items:
        ext = det_file_type(django_symlink_path + item)
        if ext == 1:
            pdf_items.append(item)
        elif ext == 2: 
            image_items.append(item)
        elif ext == 3:
            video_items.append(item)
        elif ext == 4:
            epub_items.append(item)
        elif ext == 5:
            mp3_items.append(item)
        elif ext == 6:
            txt_items.append(item)
    for pdf in pdf_items:
        add_file_item(pdf, fetch_file_class('Pdf'))
    for image in image_items:
        add_file_item(image, fetch_file_class('Image'))
    for video in video_items:
        add_file_item(video, fetch_file_class('Video'))
    for epub in epub_items:
        add_file_item(epub, fetch_file_class('Epub'))
    for song in mp3_items:
        add_file_item(song, fetch_file_class('Mp3'))
    for txt in txt_items:
        add_file_item(txt, fetch_file_class('Txt'))



def fetch_file_class(name):
    print('executing fetch_file_class')
    i, j = FileClass.objects.get_or_create(class_name=name)
    return i

def add_file_item(name, class_of_file):
    print('executing add_file_item')
    f, g = FileItem.objects.get_or_create(file_name=name, file_class=class_of_file)
    f.save()





def save_uploaded_file(uploaded_file, uploaded_file_name):
    """ Writes uploaded_file to disk """
    print('executing save_uploaded_file')
    # the_static_path is where uploaded_file is saved
#   default_path = '/Users/smvamsi/static/grey/'
    new_file = the_static_path + uploaded_file_name
    with open(new_file, 'wb+') as new_file:
        for chunk in uploaded_file.chunks():
            new_file.write(chunk)
