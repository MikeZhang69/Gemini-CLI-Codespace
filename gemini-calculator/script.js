let memory = 0;
let history = [];

function appendValue(value) {
    const resultField = document.getElementById('result');
    resultField.value += value;
}

function clearDisplay() {
    document.getElementById('result').value = '';
}

function backspace() {
    const resultField = document.getElementById('result');
    resultField.value = resultField.value.slice(0, -1);
}

function calculateResult() {
    const resultField = document.getElementById('result');
    const expression = resultField.value;
    try {
        const result = eval(expression);
        resultField.value = result;
        addToHistory(expression, result);
    } catch (error) {
        resultField.value = 'Error';
    }
}

function addToHistory(expression, result) {
    const historyList = document.getElementById('history-list');
    history.push({ expression, result });
    const listItem = document.createElement('li');
    listItem.textContent = `${expression} = ${result}`;
    historyList.appendChild(listItem);
}

function clearHistory() {
    history = [];
    document.getElementById('history-list').innerHTML = '';
}

function memoryClear() {
    memory = 0;
}

function memoryRecall() {
    document.getElementById('result').value += memory;
}

function memoryAdd() {
    try {
        memory += eval(document.getElementById('result').value);
    } catch (error) {
        document.getElementById('result').value = 'Error';
    }
}

function memorySubtract() {
    try {
        memory -= eval(document.getElementById('result').value);
    } catch (error) {
        document.getElementById('result').value = 'Error';
    }
}
