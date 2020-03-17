from django import forms

class UploadFileForm(forms.Form):
    the_file = forms.FileField(label='Select a File', help_text='max. 50MB')
    class Meta:
        fields = ('the_file',)

