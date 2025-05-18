document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.getElementById('text-input');
    if (!textarea) {
        console.error('Не найдено поле ввода с id="text-input"');
        return;
    }

    // Отключаем стандартное поведение для всех кнопок клавиатуры
    document.querySelectorAll('.key').forEach(button => {
        button.addEventListener('mousedown', function(e) {
            e.preventDefault(); // Предотвращаем "залипание" фокуса
        });
    });

    // Основной обработчик кликов
    document.querySelector('.keyboard').addEventListener('click', function(e) {
        const key = e.target.closest('.key');
        if (!key) return;

        e.preventDefault();
        const char = key.getAttribute('data-char');
        const action = key.getAttribute('data-action');
        
        const startPos = textarea.selectionStart;
        const endPos = textarea.selectionEnd;
        const text = textarea.value;
        
        if (action === 'backspace') {
            if (startPos > 0) {
                textarea.value = text.substring(0, startPos - 1) + text.substring(endPos);
                textarea.selectionStart = textarea.selectionEnd = startPos - 1;
            }
        } else if (char) {
            textarea.value = text.substring(0, startPos) + char + text.substring(endPos);
            const newPos = startPos + char.length;
            textarea.selectionStart = textarea.selectionEnd = newPos;
        }
        
        textarea.focus();
        
        // пузырьки чтобы домик работал как инадо
        const inputEvent = new Event('input', { bubbles: true });
        textarea.dispatchEvent(inputEvent);
    });


});