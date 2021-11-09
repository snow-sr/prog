var scr = document.getElementById("result")

var css = document.querySelector(":root")



var calc = {
    value: null,
    operator: null,
}
//general purpose functions
function listenOperators(){
    document.getElementById("btn-clear").addEventListener("click", clear)
}

function selectOperator(operator) {

    switch (operator) {
        case "+":
            calc.value = scr.value;
            calc.operator = sum;
            scr.placeholder = calc.value
            scr.value = "";
            break;
        case "-":
            calc.value = scr.value;
            calc.operator = substract;
            scr.placeholder = calc.value
            scr.value = "";
            break;
        case "*":
            calc.value = scr.value;
            calc.operator = multiply;
            scr.placeholder = calc.value
            scr.value = "";
            break;
        case "/":
            calc.value = scr.value;
            calc.operator = divide;
            scr.placeholder = calc.value
            scr.value = "";
            break;

    }
}

function selectNum(x) {

    if (isNaN(scr.value)) {
        scr.value = x
    } else if (scr.value == 0 && scr.value != "0.") {
        scr.value = x
    } else if(scr.value == "0."){
        scr.value += x
    }
    else {
        scr.value += x
    }
}

function clear() {
    scr.value = ""
    scr.placeholder = ""
    calc.value = null
    calc.operator = null
}

function dot() {

    if(scr.value === "" || isNaN(scr.value)){
        scr.value = "0."
    }
    else if(!scr.value.includes(".")){
        scr.value = scr.value + "."
    }
  
}

function showResults() {
    if (!isNaN(scr.value) && calc.operator != null) {
        let result = calc.operator(calc.value, Number(scr.value));
        scr.value = result;
        calc.value = result;
        calc.operator = null;
    }
}

//Now, for the math functions

function sum(x, y) {
    return parseInt(x) + parseInt(y)
}

function substract(x, y) {
    return x - y
}

function multiply(x, y) {
    return x * y
}

function divide(x, y) {
    if(y == 0 || y == null || x == 0 || x == null){
        return "erro, dividir por 0 pode ter consequências fatais."
    }
    else {
    return x / y
    }
}

function showError() {
    scr.value = errorMessage
}
window.addEventListener('load', listenOperators)