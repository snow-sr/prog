
rand = document.getElementById("generateRandom").addEventListener("click", generateRandom)

function generateRandom(){
    let range = {
        "init": document.getElementById("valorInicio").value,
        "end": document.getElementById("valorFinal").value
    }

    let result = randomNumberFromRange(range.init, range.end)
    print(result)
}



function randomNumberFromRange(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
}


function printResult(res){
    const resultText = document.getElementById("Result");
    resultText.innerHTML = `<span class="detalheNumero"><strong>${res}</strong></span>`
}

function printAddList(num){
    const list = document.getElementById("list")
    list.appendChild = `<li>${num}</li>`
}