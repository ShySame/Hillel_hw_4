from django import forms

from .models import Person


class Triangle(forms.Form):
    katet1 = forms.IntegerField(label="Катет а", min_value=1)
    katet2 = forms.IntegerField(label="Катет b", min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']

        labels = {'first_name': '',
                  'last_name': '',
                  'email': '', }

        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Email address'}), }


