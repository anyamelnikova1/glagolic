document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('converter-form');
    const textarea = document.getElementById('text-input');
    const resultDiv = document.getElementById('result');

    // 1. Предотвращаем стандартную отправку формы
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        // Здесь будет обработка отправки через AJAX (если нужно)
        resultDiv.textContent = `Текст для обработки: ${textarea.value}`;
    });

    // 2. Обработка клавиш клавиатуры
    document.querySelectorAll('.key').forEach(button => {
        button.addEventListener('click', function() {
            const char = this.getAttribute('data-char');
            const action = this.getAttribute('data-action');
            
            if (action === 'backspace') {
                // Удаляем последний символ
                textarea.value = textarea.value.slice(0, -1);
            } else if (char) {
                // Вставляем символ в текущую позицию курсора
                const startPos = textarea.selectionStart;
                const endPos = textarea.selectionEnd;
                textarea.value = textarea.value.substring(0, startPos) + 
                               char + 
                               textarea.value.substring(endPos);
                // Перемещаем курсор
                textarea.selectionStart = textarea.selectionEnd = startPos + char.length;
            }
            
            // Фокусируем поле ввода
            textarea.focus();
        });
    });
});