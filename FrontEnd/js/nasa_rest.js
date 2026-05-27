export class NasaApi {

    constructor() {

        this.base_url = "http://127.0.0.1:3000";
    }

    async search_date(date) {
        try {
            
            const answer = await fetch(
                `${this.base_url}/nasa/apod/photo?date=${date}`
            );

            const data = await answer.json();

            return data;

        } catch (erro) {

            alert(`Erro de conexão: ${erro.message}`);
        }

    }

    async search_date_interval(initial_date, end_date, search_mode) {
        try {

            const answer = await fetch(
                `${this.base_url}/nasa/photos/interval?start_date=${initial_date}&end_date=${end_date}&search_mode=${search_mode}`
            );

            const data = await answer.json();

            return data;

        } catch (erro) {

            alert(`Erro de conexão: ${erro.message}`);
        }
    }

    async search_count(count) {
        try {

            const answer = await fetch(
                `${this.base_url}/nasa/apod/photos/count?count=${count}`
            );

            const data = await answer.json();

            return data;

        } catch (erro) {

            alert(`Erro de conexão: ${erro.message}`);
        }
    }

    async search_thumbs(thumbs) {
        try {

            const answer = await fetch(
                `${this.base_url}/nasa/apod/photos/thumbs?thumbs=${thumbs}`
            );

            const data = await answer.json();

            return data;

        } catch (erro) {

            alert(`Erro de conexão: ${erro.message}`);
        }
    }
}

