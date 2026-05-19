const resultado = document.getElementById("search_result");

document.getElementById("search_data")
.addEventListener("click", async () => {

    const data = document.getElementById("data_field").value;

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

        console.log("dados da chamada rest search_result:", dados);

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

const resultadoIntervalo = document.getElementById("search_result_interval");

document.getElementById("search_date_range")
    .addEventListener("click", async () => {

        const dataInicial =
            document.getElementById("initial_date_field").value;

        const dataFinal =
            document.getElementById("end_date_field").value;

        if (!dataInicial || !dataFinal) {

            alert("Informe as datas");

            return;
        }

        try {

            const resposta = await fetch(
                `http://127.0.0.1:3000/nasa/asteroids?start_date=${dataInicial}&end_date=${dataFinal}`
            );

            const dados = await resposta.json();

            console.log("dados da chamada rest search_result_interval:", dados);

            const objetos = dados.near_earth_objects;

            console.log(objetos);

        } catch (erro) {
            console.log("Erro:", erro);
        }

    });

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

