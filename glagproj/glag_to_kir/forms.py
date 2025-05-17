from django import forms

class TextForm(forms.Form):
    text = forms.CharField(
        label='Введите текст',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ввщ старослав....'
        }),
        required=False
    )