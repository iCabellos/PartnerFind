from django import forms
from .models import UserModel


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'user_email', 'phone_number', 'in_game_name']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['class'] = 'datepicker'
