# Purpose of this file:
# This file holds all your app's form models(Forms are defined as models in Django, So you can write them in models.py if you want)
# But it's Cleaner writing forms in forms.py
from django import forms

# This form has only one field. That's a field for uploading files.
class UploadFileForm(forms.Form):
    the_file = forms.FileField(label='Select a File', help_text='max. 50MB')
    class Meta:
        fields = ('the_file',)

