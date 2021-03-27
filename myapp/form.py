from django import forms
from .models import User


class StudentRagistation(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','password')

    def __init__(self, *args, **kwargs):
        super(StudentRagistation, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
