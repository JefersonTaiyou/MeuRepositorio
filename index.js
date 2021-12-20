let nome, sobrenome;
let nomeComposto = nome + sobrenome;
const pi = 3.1415

// Comentarios

/* 
 * Documentação
 * 
 *  Tab => espaço pra frente
 *  Shift Tab => espaço pra tras
 * 
 *  typeof => verifica o tipo de dado da variavel
 * 
 *  Estrutura de Dados: é o que organiza e da estrutura aos dados do sistema/ 
 *                                          administra e da regras para os dados se comportarem
 *  => FIFO: Primeiro a Entrar/Primeiro a Sair(Fila) 
 *  => LIFO: Ultimo a Entrar/Primeiro a Sair(Pilha) 
 * 
 * 
 */

if (nome != undefined) {
    console.log(nome);
    console.log(sobrenome);
    console.log(nomeComposto);
} else {
    console.log("Sem Dados");
}

console.log(nomeComposto || "Sem Dados");

let nam = `oieeee`;
//console.log(Number.isInteger(pi));
console.log(typeof(nam));
console.log(nam.charAt(0));
console.log(nam.charCodeAt(1));
console.log(nam.indexOf('e'));
console.log(nam.substring(2));

const template = `Meu nome é ${nome}`
const up = texto => texto.toUpperCase() //função em template

console.log(`Função: ${up(template)}`);

const lista = [];

if (lista[0] == undefined) {
    lista[0] = "Primeiro Valor"
    lista.push("Segundo Valor", "terceiro", "quarto", "quinto")
}

console.log(lista[0], lista, lista.length)
lista.pop()
console.log(lista)
console.log(lista);
console.log(lista[0])
    //lista.shift();

//trabalhando com estrutura de dados:
/*
 * lista.pop() => remove o ultimo item adicionado na lista
 * util para trabalhar com conceito de LIFO/PILHA
 * delete lista[0] => remove o primeiro item da lista
 * deixa o primeiro item vazio - util para conceito de FIFO/FILA
 *
 */

//FIFO
delete lista[0];
if (lista[0] == undefined && lista[1] != undefined) {
    console.log(lista[0], lista[1])
    for (var i = 0; i < lista.length; i++) {
        lista[i] = lista[i + 1]
        delete lista[i + 1]
    }
    lista.pop();
}

console.log(lista)

const produto = {} // => objeto
produto.nome = 'Arroz';
produto.preco = 5.90;

const produto2 = {
    nome: 'Feijao',
    preco: 3.70
}

const ref = produto2;
let val = 3;
let valRef = val;

console.log(produto2);
console.log(ref);
console.log(val);
console.log(valRef);

ref.nome = 'Batata';
valRef = 5;

console.log(produto2);
console.log(ref);
console.log(val);
console.log(valRef);

function soma(a = 0, b = 0) {
    console.log(a + b);
}
soma();
soma(2, 2);

function somar(a = 0, b = 0) {
    return a + b;
}
console.log(somar());

const imprimirSoma = (a = 0, b = 0) => console.log(a + b)
imprimirSoma(5, 8);



/*
 * Atribuição por valor X Atribuição por referência
 * e.g:
 * const produto recebe a referência de um endereço de memória do objeto
 * const ref não recebe o valor do objeto e sim o mesmo endereço de memória
 * ou seja, se o objeto que está na memória mudar seu valor, tanto a const produto
 * quanto a const ref irão ter a mesma alteração que houve no objeto, já que ambas
 * referenciam o endereço de memória
 * 
 * já a const val recebe um valor em especifico/primitivo e não uma
 * referencia de memória, o que significa que o valor de val
 * é exatamente o que está sendo atribuido à ele
 * portanto a valRef quando recebe val, cria uma cópia do valor
 * de val e ambas contêm valores independentes, ou seja, caso
 * o valor de val mudar, o valor de valRef, permanece o mesmo
 * 
 * por este motivo que qdo alterado o valor do objeto nome, ref e produto
 * sofreram alterações iguais e qdo alterado valor de valRef, val permaneceu como estava
 * 
 */