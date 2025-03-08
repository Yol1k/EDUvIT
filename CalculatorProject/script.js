const display = document.getElementById('display');
const history = document.getElementById('history');

function appendToDisplay(value) {
    display.value += value;
  }

function clearDisplay() {
    display.value = '';
  }

function calculate() {
    try {
      const result = eval(display.value);
      display.value = result;
      addToHistory(display.value);
    } catch (error) {
      display.value = 'Ошибка';
    }
  }

  function appendToDisplay(value) {
    const currentValue = display.value;
    const lastChar = currentValue[currentValue.length - 1];

    const isLastCharOperator = ['+', '-', '*', '/'].includes(lastChar);

    const isNewCharOperator = ['+', '-', '*', '/'].includes(value);

    const isNewCharDot = value === '.';


    if (isNewCharDot) {
        const lastNumber = currentValue.split(/[\+\-\*\/]/).pop();
        if (lastNumber.includes('.') || isLastCharOperator) {
            return;
        }
    }
    if (isNewCharOperator && isLastCharOperator) {
        display.value = currentValue.slice(0, -1) + value;
    } else {
        display.value += value;
    }
}

function addToHistory(result) {
    const historyEntry = document.createElement('div');
    historyEntry.textContent = display.value + " = " + result;
    history.appendChild(historyEntry);
    history.scrollTop = history.scrollHeight;
    }