from django import forms

class TextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Ваш старослав.....',
            'maxlength': '1000'  # HTML-атрибут для ограничения ввода
        }),
        max_length=1000,  # Валидация на сервере
        help_text="Максимальная длина текста - 1000 символов"
    )