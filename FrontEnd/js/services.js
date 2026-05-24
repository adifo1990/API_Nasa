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

/*NeoWs*/

document.getElementById("BuscarIntervalo")
.addEventListener("click", async () => {

    const dataInicial = document.getElementById("CampoDataInicial").value;
    const dataFinal = document.getElementById("CampoDataFinal").value;

    console.log("Data enviada:", dataInicial);

    if (!dataInicial) {
        alert("Informe uma data inical");
        return;
    }
    if (!dataFinal) {
        alert("Informe uma data final");
        return;
    }

    try {
        console.log(dataInicial);

        const resposta = await fetch(
           `https://api.nasa.gov/neo/rest/v1/feed?start_date=${dataInicial}&end_date=${dataFinal}`
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
        <div>
            <h3>${dados.title}</h3>

            <img 
                src="${dados.url}" 
                alt="${dados.title}"
                width="500"
            >
        </div>
    `;
}
