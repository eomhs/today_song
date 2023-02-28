from django import forms
from todaysong.models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['singer', 'name']
        widgets = {
            'singer': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'singer': '가수',
            'name': '노래 이름',
        }  