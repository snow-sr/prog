const button = document.getElementById("submit").addEventListener("click", calculate);
const result  = document.getElementById("result")

function calculate() {

  let valorDeA = document.getElementById("VA");
  let valorDeB = document.getElementById("VB");
  let valorDeC = document.getElementById("VC");

  let res = baskara(valorDeA.value, valorDeB.value, valorDeC.value)

  res ? result.innerHTML = `X1: ${res.x1.toFixed(3)}, X2: ${res.x2.toFixed(3)}` : result.innerHTML = "Inexistentes!"

};


function baskara(a, b, c) {
  const delta = (b*b) -( 4 * a * c)

  if (delta < 0) {

   return false;

  } ;

  let result = {
      x1: (-b + Math.sqrt(delta)) / (2 * a),
      x2: (-b - Math.sqrt(delta)) / (2 * a)
  };

  return result

}