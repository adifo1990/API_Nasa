const resultado = document.getElementById("search_result_apod");

document.getElementById("search_data_apod")
.addEventListener("click", async () => {

    const date = document.getElementById("data_field_apod").value;

    console.log("Data enviada:", date);

    if (!date) {

        alert("Informe uma data");

        return;
    }

    const minDate = new Date("1995-06-16");

    const currentDate = new Date()
    .toISOString()
    .split("T")[0];

    const selectedDate = new Date(date);

    if (selectedDate < minDate) {

        alert(
            "A data deve ser maior ou igual a 1995-06-16"
        );

        return;
    }

    if (selectedDate > currentDate) {

        alert(
            "A data não pode ser maior que a atual"
        );

        return;
    }

    try {
        console.log(date);

        const resposta = await fetch(
            `http://127.0.0.1:3000/nasa/apod/photo?date=${date}`
        );

        const data = await resposta.json();

        console.log("dados da chamada rest search_result_apod:", data);

        showImage(data);

    } catch (erro) {

        console.log("Erro:", erro);

    }

});


function showImage(data) {

    resultado.innerHTML = `
    
        <h3>${data.title}</h3>

        <img 
            src="${data.url}" 
            alt="${data.title}"
            width="500"
        >
    `;
}

const resultadoIntervalo = document.getElementById("search_result_apod");

document.getElementById("search_date_range_apod")
    .addEventListener("click", async () => {

        const dataInicial =
            document.getElementById("initial_date_field_apod").value;

        const dataFinal =
            document.getElementById("end_date_field_apod").value;

        if (!dataInicial || !dataFinal) {

            alert("Informe as datas");

            return;
        }

        try {

            const resposta = await fetch(
                `http://127.0.0.1:3000/nasa/apod/photos/interval?start_date=${dataInicial}&end_date=${dataFinal}`
            );

            const dados = await resposta.json();

            console.log("dados da chamada rest search_result_interval:", dados);

            const objetos = dados.near_earth_objects;

            console.log(objetos);

        } catch (erro) {
            console.log("Erro:", erro);
        }

    });

