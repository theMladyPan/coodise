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


class ToolForm(forms.Form):
    """Tool form template."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self):
        cleaned_data = super().clean()


class DeleteFileForm(ToolForm):
    """Form for deleting files or directories."""

    tool = forms.CharField(initial="delete_file", widget=forms.HiddenInput())
    item_to_delete = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = 'id-delete-file'


class CreateDirForm(ToolForm):
    """Form for creating new directory."""

    dir_name = forms.CharField(label='Name for new directory', max_length=255)
    tool = forms.CharField(initial="create_dir", widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = 'id-create-dir'


class CreateFileForm(ToolForm):
    """Form for creating new empty file."""

    file_name = forms.CharField(
        label='Name for new empty file', max_length=255)
    tool = forms.CharField(initial="create_file", widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = 'id-create-file'


class UploadFileForm(ToolForm):
    """Form for uploading file."""

    file = forms.FileField()
    file_name = forms.CharField(
        required=False, max_length=255, label="Optional name for file")
    tool = forms.CharField(initial="upload_file", widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = 'id-upload-file'


class RenameForm(ToolForm):
    """Form for renamig."""

    new_name = forms.CharField(max_length=255, label="New name")
    tool = forms.CharField(initial="rename_file", widget=forms.HiddenInput())
    old_name = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = 'id-rename'
