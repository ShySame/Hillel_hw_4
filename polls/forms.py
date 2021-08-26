from django import forms


class Triangle(forms.Form):
    katet1 = forms.IntegerField(label="Катет а", min_value=1)
    katet2 = forms.IntegerField(label="Катет b", min_value=1)
