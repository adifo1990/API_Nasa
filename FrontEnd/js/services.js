const resultado = document.getElementById("resultadoBusca");

document.getElementById("BuscarData")
.addEventListener("click", async () => {

    const data = document.getElementById("CampoData").value;

    console.log("Data enviada:", data);

    if (!data) {
        alert("Informe uma data");
        return;
    }

    try {
        console.log(data);

        const resposta = await fetch(
            `http://127.0.0.1:3000/nasa/apod/fotos?date=${data}`
        );

        const dados = await resposta.json();

        console.log("dados da chamada rest:", dados);

        mostrarImagem(dados);

    } catch (erro) {

        console.log("Erro:", erro);

    }

});


function mostrarImagem(dados) {

    resultado.innerHTML = `
    
        <h3>${dados.title}</h3>

        <img 
            src="${dados.url}" 
            alt="${dados.title}"
            width="500"
        >
    `;
}

/*function mostrarImagem(dados) {

    resultado.innerHTML = `
    
        <h2>${dados.title}</h2>

        <img 
            src="${dados.url}" 
            alt="${dados.title}"
            width="500"
        >

         <p>${dados.explanation}</p>

    `;}*/