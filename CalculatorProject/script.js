const display = document.getElementById('display');
const history = document.getElementById('history');

// Очищаем экран
function clearDisplay() {
    display.value = '';
  }

// Вычисляем значение выражения
function calculate() { 
    try {
      const result = eval(display.value);
      addToHistory(result);
    } catch (error) {
      display.value = 'Ошибка';
    }
  }

  // Добавляем символы на экран
  function appendToDisplay(value) { 
    const currentValue = display.value;
    const lastChar = currentValue[currentValue.length - 1];
    const lastNumber = currentValue.split(/[\+\-\*\/]/).pop();

    const isLastCharOperator = ['+', '-', '*', '/'].includes(lastChar);
    const isNewCharOperator = ['+', '-', '*', '/'].includes(value);
    const isLastCharDigit = /\d/.test(lastChar);
    const isNewCharDigit = /\d/.test(value);
    const isNewCharZero = value === '0';
    const isNewCharDot = value === '.';

    // Обработка точки
    if (isNewCharDot && (lastNumber.includes('.') || isLastCharOperator || currentValue === '')) {
        return;
    }

    // Обработка нуля
    if (isNewCharZero) {
        if (!(isLastCharOperator || isLastCharDigit || lastChar === '.' || currentValue === '' || lastNumber.includes('.') || lastNumber[0] !== '0')) {
            return;
        }
    }

    // Обработка цифр
    if (isNewCharDigit && lastNumber === '0') {
        return;
    }

    // Обработка операторов
    if (isNewCharOperator) {
        if (!(isLastCharDigit || lastChar === '0')) {
            if (isLastCharOperator) {
                display.value = currentValue.slice(0, -1) + value;
                return;
            }
            return;
        }
    }

    // Общий случай: добавление символа
    display.value += value;
}

// Добавляем выражение и результат вычислений в историю
function addToHistory(result) {
    const historyEntry = document.createElement('div');
    historyEntry.textContent = display.value + " = " + result;
    history.appendChild(historyEntry);
    history.scrollTop = history.scrollHeight;
    }