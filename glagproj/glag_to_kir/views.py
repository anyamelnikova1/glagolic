from django.shortcuts import render
from .forms import TextForm

def homee(request):
    result = None
    form = TextForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        
        def alpabet_check(text):
            IsCyrrilic = False
            IsGlagolithic = False
            cyr = ('абвгдежѕзΙиклмнопрстѹфххѠцчшщъыьѣѧѩѫѭ')
            glag = ('ⰰ ⰱ ⰲ ⰳ ⰴ ⰵ ⰶ ⰷ ⰸ ⰺ ⰻ ⰽ ⰾ ⰿ ⱀ ⱁ ⱂ ⱃ ⱄ ⱅ ⱆ ⱇ ⱈ ⱒ ⱉ ⱌ ⱍ ⱎ ⱋ ⱏ ⱏⰺ ⱐ ⱑ ⱔ ⱗ ⱘ ⱙ')
            glag = glag.split(' ')
        
            if text[0] in cyr:
                IsCyrrilic = True
            else:
                IsGlagolithic = True
        
            for letter in text:
                if letter in cyr:
                    IsCyrrilic = True
                elif letter in glag:
                    IsGlagolithic = True
        
            if IsCyrrilic == IsGlagolithic:
                result = 'ВЗБОЛТАТЬ, НО НЕ СМЕШИВАТЬ (Кириллицу и Глаголицу)'
                return result
            else:
                result = 'OK'
                return text * 2

    
    return render(request, 'home.html', {
        'form': form,
        'result': result
    })