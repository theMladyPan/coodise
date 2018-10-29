from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(forms.Form):
    """Default login form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))

    user_name = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateDirForm(forms.Form):
    """Form for creating new directory."""
    dir_name = forms.CharField(label='Name for new directory', max_length=255)
    tool = forms.CharField(initial="create_dir", widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(CreateDirForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-create-dir'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

    def clean(self):
        cleaned_data = super(CreateDirForm, self).clean()
        return cleaned_data

    def save(self):
        cleaned_data = super(CreateDirForm, self).clean()


class CreateFileForm(forms.Form):
    """Form for creating new empty file."""
    file_name = forms.CharField(
        label='Name for new empty file', max_length=255)
    tool = forms.CharField(initial="create_file", widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(CreateFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-create-file'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

    def clean(self):
        cleaned_data = super(CreateFileForm, self).clean()
        return cleaned_data

    def save(self):
        cleaned_data = super(CreateFileForm, self).clean()


class UploadFileForm(forms.Form):
    """Form for uploading file."""
    file_name = forms.CharField(max_length=255, label="Name for new file")
    file = forms.FileField()
    tool = forms.CharField(initial="upload_file", widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-upload-file'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

    def clean(self):
        cleaned_data = super(UploadFileForm, self).clean()
        return cleaned_data

    def save(self):
        cleaned_data = super(UploadFileForm, self).clean()
