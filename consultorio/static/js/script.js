//var nome = prompt('Qual o seu nome?');
const pi = 3.14;

console.log('nome: '+ nome);


//maiorIdade(prompt('Qual a sua idade?'));

function maiorIdade(idade){
    if(idade >= 18){
        alert("Maior de idade");
    } else{
        alert("Menor de idade");
    }
}

for(let i=0; i<0; i++){
    confirm('Confirme '+i+' vezes.');
}

switch (nome){
    case "Murilo":
        maiorIdade(prompt('Qual a sua idade?'));
        break;
    case "Werlon":
        alert("Pedir Revisão");
        break;
    case "Grilo":
        alert("cri cri cri cri cri cri cri");
        break;
}

function mudarTexto(texto){
    document.getElementById('campo_texto').innerText=texto;
}