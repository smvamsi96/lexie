import os
import filetype
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lexie.settings')
import django
django.setup()
from grey.models import FileClass, FileItem

path = '/Users/smvamsi/Code/lexie/grey/static/grey/'

items = os.listdir(path)

pdf_items = []
video_items = []
image_items = []
epub_items = []
undefined_items = []


def find_file_type():
    for item in items:
        file_item = filetype.guess(path + item)
        ext = file_item.extension
        if ext == 'pdf':
            pdf_items.append(item)
        elif ext == 'png' or  ext == 'jpg' or ext == 'heic' or ext == 'gif':
            image_items.append(item)
        elif ext == 'webm' or ext == 'mkv' or ext == 'mp4' or ext == 'mov' or ext == 'avi':
            video_items.append(item)
        elif ext == 'epub':
            epub_items.append(item)
        else:
            undefined_items.append(item)

def fetch_file_class(name):
    i, j = FileClass.objects.get_or_create(class_name=name)
    return i

def add_file_item(name, class_of_file):
    f, g = FileItem.objects.get_or_create(file_name=name, file_class=class_of_file)
    f.save()

def populate():
    for pdf in pdf_items:
        add_file_item(pdf, fetch_file_class('Pdf'))
    for image in image_items:
        add_file_item(image, fetch_file_class('Image'))
    for video in video_items:
        add_file_item(video, fetch_file_class('Video'))
    for epub in epub_items:
        add_file_item(epub, fetch_file_class('Epub'))
#   for song in audio_items:
#       add_file_item(song, Song)


if __name__ == '__main__':
    print("Starting LexieGrey Indexing Script")
    find_file_type()
    populate()
