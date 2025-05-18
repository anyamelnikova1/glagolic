document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('converter-form');
    const textarea = document.getElementById('text-input');
    const resultDiv = document.getElementById('result');

    // 1. Предотвращаем стандартную отправку формы
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        resultDiv.textContent = `Текст для обработки: ${textarea.value}`;
    });

    document.querySelectorAll('.key').forEach(button => {
        button.addEventListener('click', function() {
            const char = this.getAttribute('data-char');
            if (char) {
                textarea.value += char;
                textarea.focus();
            }

            
            // Фокусируем поле ввода
            textarea.focus();
        });
    });
});