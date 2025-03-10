const display = document.getElementById('display');
const history = document.getElementById('history');

function clearDisplay() { //очищаем экран
    display.value = '';
  }

function calculate() { //вычисления
    try {
      const result = eval(display.value);
      addToHistory(result);
    } catch (error) {
      display.value = 'Ошибка';
    }
  }

  function appendToDisplay(value) { //добавляем результат на экран
    const currentValue = display.value;
    const lastChar = currentValue[currentValue.length - 1];

    const isLastCharOperator = ['+', '-', '*', '/'].includes(lastChar);

    const isNewCharOperator = ['+', '-', '*', '/'].includes(value);

    const isLastCharDigit = ['1', '2', '3', '4', '5', '6', '7', '8', '9'].includes(lastChar);

    const isNewCharDigit = ['1', '2', '3', '4', '5', '6', '7', '8', '9'].includes(value);

    const isNewCharZero = value === '0';

    const isNewCharDot = value === '.';

    if (isNewCharDot) {
        const lastNumber = currentValue.split(/[\+\-\*\/]/).pop();
        if (lastNumber.includes('.') || isLastCharOperator || currentValue === '') {
            return;
        }
    }
    
    if (isNewCharZero) {
      const lastNumber = currentValue.split(/[\+\-\*\/]/).pop();
      if (isLastCharOperator || isLastCharDigit || lastChar === '.' || currentValue === '' || lastNumber.includes('.') || lastNumber[0] !== '0') {
        display.value += value;
        return;
      }
      else if (lastChar === '0') {
        return;
      }
      else {
        return;
      }
    }
    if (isNewCharDigit) {
      const lastNumber = currentValue.split(/[\+\-\*\/]/).pop(); // Получаем последнее число
      if (lastNumber === '0') {
          return;
      }
      display.value += value;
      return;
    }

    if (isNewCharOperator) {
      if (isLastCharDigit || lastChar === '0') {
        display.value += value;
        return;
      }
      else if (isLastCharOperator) {
        display.value = currentValue.slice(0, -1) + value; 
      }
      else {
        return;
      }
    }
    else {
      display.value += value;
    }
}

function addToHistory(result) { //добавляем в историю
    const historyEntry = document.createElement('div');
    historyEntry.textContent = display.value + " = " + result;
    history.appendChild(historyEntry);
    history.scrollTop = history.scrollHeight;
    }