function tables(){

    var name = document.getElementById('nometabela')
    
    var birth = document.getElementById('birthtabela')

    var num = document.getElementById('numtabela')

    var email = document.getElementById('emailtabela')

    var rg = document.getElementById('rgtabela')

    var filme = document.getElementById('filmetabela')

    var music = document.getElementById('musicatabela')

    //inputs
    var inputNome = document.getElementById('name').value

    var inputBirth = document.getElementById('Birth').value 

    var inputTel = document.getElementById('Tel').value 

    var inputEmail = document.getElementById('email').value 

    var inputRg = document.getElementById('reggeral').value 

    var inputfilm = document.getElementById('film').value

    var inputMusic = document.getElementById('music').value 
        
    //change
    name.innerHTML = inputNome;
    birth.innerHTML = inputBirth;
    num.innerHTML = inputTel;
    email.innerHTML = inputEmail;
    rg.innerHTML = inputRg;
    filme.innerHTML = inputfilm;
    music.innerHTML = inputMusic;

}
