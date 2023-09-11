from xml.dom import ValidationErr
from django import forms

def valid(value):
    if value[0].lower()=='h' and len(value)<6 :
        raise forms.ValidationError('name starts with h')

class Studentform(forms.Form):
    Sname = forms.CharField(max_length=123,validators=[valid])
    Sid = forms.IntegerField()
    Sage = forms.IntegerField()
    Semail = forms.EmailField(validators=[valid])
