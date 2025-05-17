from django import forms

class TextConversionForm(forms.Form):
    input_text = forms.CharField(
        label='Введите текст',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Введите текст для преобразования...'
        }),
        required=True
    )