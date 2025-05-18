from django.shortcuts import render
from .forms import TextForm
from asgiref.sync import sync_to_async
from django.http import HttpRequest

# Асинхронная обертка для рендеринга
@sync_to_async
def render_template(request, template, context):
    return render(request, template, context)

async def homee(request: HttpRequest):
    result = None
    
    if request.method == 'POST':
        # Создаем копию POST данных для асинхронной обработки
        post_data = request.POST.dict() if hasattr(request.POST, 'dict') else {}
        form = TextForm(post_data)
        
        # Проверка валидности формы
        is_valid = await sync_to_async(form.is_valid)()
        
        if is_valid:
            text = form.cleaned_data['text']
            result = await process_text(text)
    else:
        form = TextForm()
    
    return await render_template(request, 'home.html', {
        'form': form,
        'result': result
    })

async def process_text(text: str) -> str:
    """Асинхронная обработка текста"""
    if not text:
        return None
        
    cyr = set('абвгдежѕзιиклмнопрстѹфхѡцчшщъыьѣѧѩѫѭ')
    glag = set('ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰊⰋⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰜⰝⰞⰟⰟⰊⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙ')
    has_cyr = False
    has_glag = False
    for char in text:
        try:
            if char.lower() in cyr:
                has_cyr = True
            if char in glag:
                has_glag = True
        except:
            continue
        if has_cyr and has_glag:
            break
    
    if has_cyr and has_glag:
        return 'ВЗБОЛТАТЬ, НО НЕ СМЕШИВАТЬ (Кириллицу и Глаголицу)'
    else:
        return "все норм\n" + text 