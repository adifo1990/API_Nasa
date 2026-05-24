import { NasaApi } from "./nasa_rest.js";

const nasa_api = new NasaApi();

const resultado = document.getElementById("search_result_apod");

const search_mode = document.getElementById("search_mode");

const sections = {
    date: document.getElementById("search_by_date"),
    interval: document.getElementById("search_by_interval"),
    count: document.getElementById("search_by_count"),
    thumbs: document.getElementById("search_by_thumbs")
};

function validate_date(date) {

    console.log("Data enviada:", date);

    if (!date) {

        alert("Informe uma data");

        return false;
    }

    const min_date = "1995-06-16";

    const today = new Date().toISOString().split("T")[0];

    if (date < min_date) {

        alert("A data deve ser maior ou igual a 1995-06-16");

        return false;
    }

    if (date >= today) {

        alert("A data não pode ser maior ou igual a atual");

        return false;
    }

    return true;
}

function validate_date_interval(initial_date, end_date) {

    const min_date = "1995-06-16";

    if (!initial_date || !end_date) {

        alert("Informe as datas");

        return;
    }

    const today = new Date().toISOString().split("T")[0];

    if (initial_date < min_date) {

        alert("A data inicial deve ser maior ou igual a 1995-06-16");

        return false;
    }

    if (end_date >= today) {

        alert("A data final não pode ser maior ou igual a atual");

        return false;
    }

    if (initial_date > end_date) {

        alert("A data inicial não pode ser maior que a data final");

        return false;
    }

    return true;

}

function show_images(images) {

    resultado.innerHTML = "";

    if (!Array.isArray(images)) {
        images = [images];
    }

    images.forEach((image) => {

        if (image.media_type !== "image") {
            return;
        }

        const div = document.createElement("div");

        const title = document.createElement("h3");
        title.textContent = image.title;

        const img = document.createElement("img");

        img.src = image.url;
        img.alt = image.title;
        img.width = 500;

        img.onerror = () => {

            img.remove();

            const erro = document.createElement("p");

            erro.textContent =
                "Imagem indisponível";

            div.appendChild(erro);
        };

        div.appendChild(title);
        div.appendChild(img);

        resultado.appendChild(div);
    });
}

function validate_count(count) {

    if (!count) {

        alert("Informe uma quantidade entre 1 e 100");

        return false;
    }

    if (count < 1) {

        alert("A quantidade deve ser maior ou igual a 1");

        return false;
    }

    if (count > 100) {

        alert("A quantidade deve ser menor ou igual a 100");

        return false;
    }

    return true;
}

function show_videos(videos) {

    resultado.innerHTML = "";

    if (!Array.isArray(videos)) {

        videos = [videos];
    }

    videos.forEach((video) => {

        if (video.media_type !== "video") {

            return;
        }

        const div = document.createElement("div");

        const title = document.createElement("h3");

        title.textContent = video.title;

        div.appendChild(title);

        const url = video.url;

        if (url.endsWith(".mp4")) {

            const videoElement = document.createElement("video");

            videoElement.src = url;

            videoElement.width = 500;

            videoElement.height = 300;

            videoElement.controls = true;

            div.appendChild(videoElement);
        }

        else if (
            url.includes("youtube.com")
            || url.includes("youtu.be")
        ) {

            const iframe = document.createElement("iframe");

            iframe.width = "500";

            iframe.height = "300";

            iframe.allowFullscreen = true;

            iframe.src = convertYoutubeUrl(url);

            div.appendChild(iframe);
        }

        resultado.appendChild(div);
    });
}

search_mode.addEventListener("change", () => {

    resultado.innerHTML = "";

    Object.values(sections).forEach((section) => {
        section.style.display = "none";
    });

    const selected = search_mode.value;

    if (sections[selected]) {
        sections[selected].style.display = "block";
    }
});

document.getElementById("search_date_apod")
    .addEventListener("click", async () => {

        const date = document.getElementById("data_field_apod").value;

        const is_valid_date = validate_date(date);

        if (!is_valid_date) {

            return;
        }

        show_images(
            await nasa_api.search_date(date)
        );
    });


document.getElementById("search_date_range_apod")
    .addEventListener("click", async () => {

        const initial_date =
            document.getElementById("initial_date_field_apod").value;

        const end_date =
            document.getElementById("end_date_field_apod").value;

        if (!validate_date_interval(initial_date, end_date)) {

            return;
        }

        show_images(
            await nasa_api.search_date_interval(initial_date, end_date)
        );

    });

document.getElementById("search_count_apod")
    .addEventListener("click", async () => {
        const count = document.getElementById("count_field_apod").value;

        if (!validate_count(count)) {

            return;
        }

        show_images(
            await nasa_api.search_count(count)
        );

    });

document.getElementById("search_thumbs_apod")
    .addEventListener("click", async () => {
        const thumbs = true;

        show_videos(
            await nasa_api.search_thumbs(thumbs)
        );
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
