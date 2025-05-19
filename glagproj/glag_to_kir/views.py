from django.shortcuts import render
from .forms import TextForm
from asgiref.sync import sync_to_async
from django.http import HttpRequest
from typing import Literal
import re

# Асинхронная обертка для рендеринга
@sync_to_async
def render_template(request, template, context):
    return render(request, template, context)

from typing import Literal
import re

cyr = ('а б в г д е ж ѕ з Ι и к л м н о п р с т ѹ ф х Ѡ ц ч ш щ ъ ы ь ѣ ю ѧ ѩ ѫ ѭ ꙗ')
glag = ('Ⰰ Ⰱ Ⰲ Ⰳ Ⰴ Ⰵ Ⰶ Ⰷ Ⰸ Ⰺ Ⰻ Ⰽ Ⰾ Ⰿ Ⱀ Ⱁ Ⱂ Ⱃ Ⱄ Ⱅ Ⱆ Ⱇ Ⱈ Ⱉ Ⱌ Ⱍ Ⱎ Ⱏ ⰟⰊ Ⱐ Ⱑ Ⱓ Ⱔ Ⱕ Ⱖ Ⱗ')

def transliterate(text: str, target: Literal['cyr', 'glag']) -> str:
    cyr_to_glag = {
        "а": 'Ⰰ', "б": 'Ⰱ', "в": 'Ⰲ', "г": 'Ⰳ', "д": 'Ⰴ', "е": 'Ⰵ', "ж": 'Ⰶ', "ѕ": 'Ⰷ', "з": 'Ⰸ', "Ι": 'Ⰺ',
        "и": 'Ⰻ', "к": 'Ⰽ', "л": 'Ⰾ', "м": 'Ⰿ', "н": 'Ⱀ', "о": 'Ⱁ', "п": 'Ⱂ', "р": 'Ⱃ', "с": 'Ⱄ', "т": 'Ⱅ',
        "ѹ": 'Ⱆ', "ф": 'Ⱇ', "х": 'Ⱈ', "Ѡ": 'Ⱉ', "ц": 'Ⱌ', "ч": 'Ⱍ', "ш": 'Ⱎ', "щ": 'Ⱏ', "ъ": 'Ⱏ', "ы": 'ⰟⰊ',
        "ь": 'Ⱐ', "ѣ": 'Ⱑ', "ю": 'Ⱓ', "ѧ": 'Ⱔ', "ѩ": 'Ⱕ', "ѫ": 'Ⱖ', "ѭ": 'Ⱗ', "ꙗ": 'Ⱑ', " ": ' '
    }

    glag_to_cyr = {
        "Ⰰ": 'а', "Ⰱ": 'б', "Ⰲ": 'в', "Ⰳ": 'г', "Ⰴ": 'д', "Ⰵ": 'е', "Ⰶ": 'ж', "Ⰷ": 'ѕ', "Ⰸ": 'з', "Ⰺ": 'Ι',
        "Ⰻ": 'и', "Ⰽ": 'к', "Ⰾ": 'л', "Ⰿ": 'м', "Ⱀ": 'н', "Ⱁ": 'о', "Ⱂ": 'п', "Ⱃ": 'р', "Ⱄ": 'с', "Ⱅ": 'т',
        "Ⱆ": 'ѹ', "Ⱇ": 'ф', "Ⱈ": 'х', "Ⱉ": 'Ѡ', "Ⱌ": 'ц', "Ⱍ": 'ч', "Ⱎ": 'ш', "Ⱏ": 'щ', "ⰟⰊ": 'ы',
        "Ⱐ": 'ь', "Ⱑ": 'ѣ', "Ⱓ": 'ю', "Ⱔ": 'ѧ', "Ⱕ": 'ѩ', "Ⱖ": 'ѫ', "Ⱗ": 'ѭ', " ": ' '
    }

    word = ' '
    newtext = (list(text))
    for letter in newtext:
        word += letter + ' '

    if target == 'cyr':
        target_word = ''
        for letter in word:
            target_word += glag_to_cyr.get(letter, letter)
        converteds = target_word.split('   ')
        final = ' '.join([''.join(converted.split()) for converted in converteds])

        if 'ъΙ' in final:
            final = final.replace('ъΙ', 'ы')

        final = re.sub(r'\bѣ', 'ꙗ', final)
        return final
    elif target == 'glag':
        target_word = ''
        for letter in word:
            target_word += cyr_to_glag.get(letter.lower(), letter)
        converteds = target_word.split('   ')
        final = ' '.join([''.join(converted.split()) for converted in converteds])
        return final

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
    elif has_cyr:
        return await sync_to_async(transliterate)(text, 'glag')
    elif has_glag:
        return await sync_to_async(transliterate)(text, 'cyr')
    