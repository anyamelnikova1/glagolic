document.addEventListener('DOMContentLoaded', () => {
    console.log('Документ загружен');
    
    const textarea = document.getElementById('text-input');
    if (!textarea) {
      return;
    }
  
    const keys = document.querySelectorAll('.key');
    if (keys.length === 0) {
      return;
    }

    keys.forEach(key => {
      key.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
      
        
        const char = key.dataset.char;
        const action = key.dataset.action;
        const startPos = textarea.selectionStart;
        const endPos = textarea.selectionEnd;
        const text = textarea.value;
        // удаление букав
        if (action === 'backspace') {
          if (startPos > 0) {
            textarea.value = text.substring(0, startPos-1) + text.substring(endPos);
            textarea.selectionStart = textarea.selectionEnd = startPos-1;
          }
          // прибавление букав
        } else if (char) {
          textarea.value = text.substring(0, startPos) + char + text.substring(endPos);
          const newPos = startPos + char.length;
          textarea.selectionStart = textarea.selectionEnd = newPos;
        }
  
        textarea.focus();
        

      });
    });
  });