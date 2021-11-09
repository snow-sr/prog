let altura = document.getElementById('height')
let peso = document.getElementById('Weight')
const btn = document.getElementById('button')
const result = document.getElementById('display')
let yourImc = null
btn.onclick = () => {
   var alt = altura.value/100
   var pes = peso.value

   var imc = pes/(alt*alt)

   console.log(imc)

   if(imc <= 18.5){
      yourImc = 'Abaixo do Peso'
      color='bg-warning'
   }
   else if(imc > 18.5 && imc <= 24.9){
      yourImc = 'Peso Ideal'
      color='bg-sucess'
   }
   else if(imc >= 25 && imc <=29.9){
      yourImc = 'Sobrepeso'
      color='bg-warning'
   }
   else if(imc >=30 && imc <=34.9){
      yourImc = 'Obesidade grau I'
      color='bg-danger'
   }
   else if(imc >=35 && imc <=39.9){
      yourImc = 'Obesidade grau II'
      color='bg-danger'
   }
   else{
      yourImc = 'Obesidade grau III'
      color='bg-danger'
   }

   result.innerHTML= `<p class='${color}'>${yourImc}</p>`
}
