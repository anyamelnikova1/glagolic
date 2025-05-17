from django.shortcuts import render
from .forms import TextForm

def homee(request):
    result = None
    form = TextForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        result = text.upper()
    
    return render(request, 'home.html', {
        'form': form,
        'result': result
    })