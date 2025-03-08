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

function addToHistory(result) {
    const historyEntry = document.createElement('div');
    historyEntry.textContent = display.value + " = " + result;
    history.appendChild(historyEntry);
    history.scrollTop = history.scrollHeight;
    }