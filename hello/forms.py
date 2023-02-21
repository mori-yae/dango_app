from django import forms #☆
from.models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False,\
            widget=forms.TextInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
    str = forms.CharField(label='String', \
        widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_date = super().clean()
        str = cleaned_date['str']
        if(str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')