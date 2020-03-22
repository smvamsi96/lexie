import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lexie.settings')
import django
django.setup()
from grey.models import FileClass, FileItem

django_symlink_path = '/Users/smvamsi/Code/lexie/grey/static/grey/'

all_classes = ['Videos', 'Images', 'Books', 'AudioFiles', 'Documents', 'Apps', 'CompressedFiles', 'UnrecognizedFiles',]

def add_file_class(name):
    f = FileClass.objects.get_or_create(class_name=name)[0]
    f.save()

def populate():
    for file_class in all_classes:
        add_file_class(file_class)


if __name__ == '__main__':
    print("Starting LexieGrey Class Population Script")
    populate()
